import os
import numpy as np
import pandas as pd
import mne

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
# -----------------------------
# 1. Load Metadata and Map Labels
# -----------------------------
metadata = pd.read_csv('Dataset/participants.tsv', sep='\t')
print(metadata.head())

group_mapping = {'A': 0, 'F': 1, 'C': 2}
metadata['label'] = metadata['Group'].map(group_mapping)
print(metadata[['participant_id', 'Group', 'label']].head())

subject_labels = dict(zip(metadata['participant_id'], metadata['label']))

# -----------------------------
# 2. Define Paths and Initialize Containers
# -----------------------------
derivatives_path = os.path.join('Dataset', 'derivatives')
subject_folders = [os.path.join(derivatives_path, d) for d in os.listdir(derivatives_path) if d.startswith('sub-')]

all_features = []
all_epoch_subject_ids = []

freq_bands = {
    "delta": (0.5, 4),
    "theta": (4, 8),
    "alpha": (8, 13),
    "beta": (13, 25),
    "gamma": (25, 45),
}

# -----------------------------
# 3. Loop Over All Subject Folders and Process EEG Data
# -----------------------------
for subject_folder in subject_folders:
    eeg_folder = os.path.join(subject_folder, 'eeg')
    set_files = [f for f in os.listdir(eeg_folder) if f.endswith('.set')]
    if not set_files:
        continue
    
    set_file_path = os.path.join(eeg_folder, set_files[0])
    print("Loading:", set_file_path)
  
    raw = mne.io.read_raw_eeglab(set_file_path, preload=True)
    raw.filter(0.5, 45, fir_design='firwin')
    # Create fixed-length epochs (2 seconds duration, 1 second overlap)
    epochs = mne.make_fixed_length_epochs(raw, duration=2.0, overlap=1, preload=True)
    # Use the events array length since bad epochs may not be dropped:
    psd = epochs.compute_psd(method="welch", fmin=0.5, fmax=45)
    psds, freqs = psd.get_data(return_freqs=True)
    
    band_power = {}
    for band, (fmin, fmax) in freq_bands.items():
        idx = np.logical_and(freqs >= fmin, freqs <= fmax)
        band_power[band] = psds[:, :, idx].mean(axis=-1)
      
    bp_abs = np.stack(list(band_power.values()), axis=-1)
    total_power = bp_abs.sum(axis=-1, keepdims=True)
    rbp_relative = bp_abs / total_power
    features = rbp_relative.reshape(rbp_relative.shape[0],
                                    rbp_relative.shape[1],
                                    rbp_relative.shape[2], 1)
    
    all_features.append(features)
    subject_id = os.path.basename(subject_folder)
    num_epochs = features.shape[0]
    all_epoch_subject_ids.extend([subject_id] * num_epochs)


# Concatenate features across all subjects
X = np.concatenate(all_features, axis=0)
n_channels, n_freqs, n_times = X.shape[1:]
y = np.array([subject_labels[pid] for pid in all_epoch_subject_ids])

# --------new
# Reshape for scaling: (n_epochs, n_channels, n_freqs, n_times) → (n_epochs, -1)
X_reshaped = X.reshape(X.shape[0], -1)

# Split into training and test sets (assuming y is defined appropriately)
X_train, X_test, y_train, y_test = train_test_split(X_reshaped, y, test_size=0.2, random_state=42)
# Fit scaler on training data only
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Reshape back to original shape
X_train = X_train.reshape(X_train.shape[0], n_channels, n_freqs, n_times)
X_test = X_test.reshape(X_test.shape[0], n_channels, n_freqs, n_times)

print("Final training feature shape:", X_train.shape)
print("Final test feature shape:", X_test.shape)
print("Final label vector shape:", y.shape)

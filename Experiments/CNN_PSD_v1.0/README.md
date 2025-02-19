# EEG-ML-Experiment: EEG-Based Alzheimer’s Detection Prototype

This repository contains an implementation of a deep learning pipeline for detecting early signs of Alzheimer’s disease using EEG signals. The model integrates ideas from established research and public implementations, and it has been adapted and adjusted for experimental purposes. While this prototype is part of my ongoing research exploration, it serves primarily as a proof-of-concept and learning tool.

---

## Overview

Alzheimer’s disease is a major neurodegenerative disorder that affects millions globally. Traditional diagnostic techniques are often invasive and expensive. This project explores a non-invasive alternative by leveraging EEG data, which records the brain's electrical activity, and applying deep learning to extract meaningful spectral features. By focusing on power spectral density (PSD) and relative band power (RBP) across key frequency bands, the model aims to capture EEG biomarkers that may indicate early signs of Alzheimer’s.

---

## How It Works

### Data Preprocessing

The preprocessing pipeline converts raw EEG recordings into structured features:
- **Data Loading and Label Mapping:**  
  Participant metadata is loaded from a TSV file, mapping diagnostic groups (A for Alzheimer’s, F for Frontotemporal Dementia, C for healthy controls) to numeric labels. This step is crucial for supervised learning.
  
- **EEG Signal Processing:**  
  Using MNE-Python, raw EEG data is filtered (0.5–45 Hz) to remove noise, and the continuous recordings are segmented into 2-second epochs with 1-second overlap. This segmentation captures transient neural patterns relevant to Alzheimer’s.

### Feature Extraction

For each epoch, Welch’s method is applied to compute the power spectral density (PSD). The code then extracts relative band power (RBP) features for standard EEG frequency bands (delta, theta, alpha, beta, gamma). This produces a 4D tensor (epochs, channels, bands, 1) that serves as the input to the deep learning model.

### Model Architecture

The deep learning model is inspired by established CNN-based approaches and architectures such as DICE‑Net. It uses convolutional layers—including depthwise and separable convolutions—to learn spatial and spectral patterns from the RBP features. Although the model builds on previous work, several modifications and adjustments have been implemented to suit this specific experimental setup.

---


## Citations

- **DICE‑Net:**  
  The model architecture also draws on ideas from the DICE‑Net paper:  
  *DICE‑Net: A Novel Convolution-Transformer Architecture for Alzheimer Detection in EEG Signals.*

- **OpenNeuro (2020):**
  Alzheimer's EEG Dataset [Dataset]. Available at: [openneuro datasets](https://doi.org/10.18112/openneuro.ds004504.v1.0.8) .

- **Sangmandu (2021):**
   'CNN 모델 구현 및 성능 향상 기본 기법 적용하기'.Available at: [sangmandu gitbook](https://sangmandu.gitbook.io/til/til_ml/cnn-fundamental/5) .

  
---

## Final Notes

This repository is part of my ongoing research efforts to explore EEG-based biomarkers for Alzheimer’s detection. Although the current prototype is experimental and may not yet reach clinical accuracy standards, it has been a valuable project for learning and skill development. Future work will focus on further refining the model and integrating additional features.

Feel free to explore, experiment, and provide feedback. Contributions are welcome!

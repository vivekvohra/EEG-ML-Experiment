# EEG-ML-Experiment

Welcome to the EEG-ML-Experiment repository! This repository is dedicated to exploring various experimental models for processing EEG data using deep learning techniques. The overall goal is to develop and test different approaches for tasks like Alzheimer’s detection using EEG signals. Although these projects are experimental, they serve as an important learning tool and a foundation for future research and development.

---

## Overview

This repository contains multiple experimental models, each implemented in its own subdirectory along with a dedicated README file. The main focus is on leveraging EEG data—specifically, features extracted from power spectral density (PSD) and relative band power—for diagnostic purposes. This work is part of my ongoing research efforts, and while the models are still in development and experimental in nature, they represent a significant learning experience in applying machine learning to biomedical signals.

## Related Blog Post

I wrote a blog post detailing the above.  
Read the full post here: [Detecting Alzheimer’s with EEG and Deep Learning – Part 1](https://dev.to/vivekvohra/part-1-detecting-alzheimers-with-eeg-and-deep-learning-theory-motivation-and-preprocessing-1hd1)

Post for 2nd model:[Detecting Alzheimer’s Disease using a CNN-BiLSTM Architecture](https://dev.to/vivekvohra/detecting-alzheimers-disease-with-eeg-and-deep-learning-3ifh)


---

## Repository Structure

The repository is organized as follows:

```
EEG-ML-Experiment/
│
├── README.md                # This file, providing an overview of the repository
├── requirements.txt         # List of Python dependencies for the project
├── .gitignore               # Files and directories to be ignored by Git
│
└── experiments/             # Contains multiple experimental models
    ├── EEGNet_Modified/     # Example experimental model based on a modified EEGNet architecture
    │   ├── model.py         # Model definition
    │   ├── train.py         # Code for training the model
    │   └── README.md        # Detailed description for this model
    │    └── EEG_Exploration.ipynb              # Jupyter notebook
    │
    ├── EEG_CNN-BiLSTM     
    │   ├── conference.pdf    # Conference Submission (ICDSINC 2025)     
    │   └── adsa.ipynb        # Jupyter notebook
    │         
    │
    └── Other_Model/         
        ├── model.py
        ├── train.py
        └── README.md
```

Each experimental model has its own folder under the `experiments/` directory. Every folder includes code files and a README that explains the approach, design choices, and results specific to that model.

---

## Final Notes

This repository is a work in progress. While the models are experimental and primarily for educational and research purposes, they showcase my ability to integrate advanced signal processing techniques and deep learning methods to address challenging problems in neuroscience. I look forward to iterating on these models and exploring new ideas as my research continues.

---

<div align="center">

# 🐱 Cat vs Dog Image Classification 🐶

### Deep Learning Image Classifier using Transfer Learning with ResNet50

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange?logo=tensorflow&logoColor=white)](https://www.tensorflow.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Git LFS](https://img.shields.io/badge/Git-LFS-blueviolet?logo=git&logoColor=white)](https://git-lfs.github.com/)

**A complete end-to-end Deep Learning workflow — from raw images to a live, deployed web app.**

**Author:** Abhash — IIT Bhubaneswar

[🌐 Live Demo](https://cnnproject-h8ekdlssc92wiz8gkuowp7.streamlit.app/) · [Report Bug](../../issues) · [Request Feature](../../issues)

</div>

---

## 📑 Table of Contents

- [About the Project](#-about-the-project)
- [Demo](#-demo)
- [Dataset](#-dataset)
- [Data Pipeline](#-data-pipeline)
- [Data Augmentation](#-data-augmentation)
- [Model Architecture](#-model-architecture)
- [Training Configuration](#-training-configuration)
- [Training Callbacks](#-training-callbacks)
- [Prediction Pipeline](#-prediction-pipeline)
- [Repository Structure](#-repository-structure)
- [Getting Started](#-getting-started)
- [Roadmap](#-roadmap)
- [Author](#-author)

---

## 📌 About the Project

This project is a **binary image classification application** that predicts whether an uploaded image is a **Cat** or a **Dog**, built using **Transfer Learning** on the pretrained **ResNet50** architecture (TensorFlow/Keras) and deployed via **Streamlit**.

It demonstrates a practical, production-style Deep Learning workflow, including:

- ✅ Data preprocessing & dataset validation
- ✅ Corrupted image detection and handling
- ✅ Data augmentation for better generalization
- ✅ Transfer learning with a ResNet50 backbone
- ✅ Model training, checkpointing & serialization
- ✅ End-to-end prediction pipeline
- ✅ Version control with Git & Git LFS
- ✅ Deployment on Streamlit Cloud

---

## 🎬 Demo

👉 **Try the live app here:**
**[https://cnnproject-h8ekdlssc92wiz8gkuowp7.streamlit.app/](https://cnnproject-h8ekdlssc92wiz8gkuowp7.streamlit.app/)**

Simply upload a `.jpg`, `.jpeg`, or `.png` image of a cat or dog, and the app returns the predicted class along with its confidence score.

---

## 📊 Dataset

The project uses a Cat vs Dog image dataset containing approximately:

| Class | Images |
|---|---:|
| 🐱 Cat | 12,497 |
| 🐶 Dog | 12,494 |

> During preprocessing, corrupted JPEG images were identified and removed to prevent errors during model training.

---

## 🔄 Data Pipeline

1. Cat and Dog images are loaded from the dataset directories.
2. Corrupted image files are identified and removed.
3. Images are resized to **224 × 224** pixels.
4. The dataset is split into training and validation sets.
5. Training images are augmented to improve generalization.
6. ResNet50-specific preprocessing is applied.
7. The pretrained ResNet50 backbone is used for feature extraction.
8. A custom classification head performs the Cat vs Dog prediction.
9. The best performing model is saved as `best_model.keras`.

---

## 🧪 Data Augmentation

The training pipeline applies the following augmentation techniques to improve robustness and reduce overfitting:

- Random Horizontal Flip
- Random Rotation
- Random Zoom
- Random Translation
- Random Contrast

---

## 🏗️ Model Architecture

The project uses **ResNet50 pretrained on ImageNet** as the feature-extraction backbone.

```text
Input Image (224 × 224 × 3)
            ↓
     Data Augmentation
            ↓
     ResNet50 Backbone
            ↓
   Global Average Pooling
            ↓
     Batch Normalization
            ↓
    Dense Layer (256)
            ↓
         Dropout
            ↓
    Output Layer (1)
            ↓
         Sigmoid
            ↓
       Cat / Dog
```

### 🔬 Transfer Learning

The pretrained ResNet50 backbone is initially **frozen** while the custom classification layers learn the Cat vs Dog task — leveraging ImageNet-learned features instead of training a CNN from scratch.

---

## ⚙️ Training Configuration

| Parameter | Value |
|---|---|
| Base Model | ResNet50 |
| Input Size | 224 × 224 |
| Batch Size | 32 |
| Optimizer | Adam |
| Learning Rate | 0.0001 |
| Loss Function | Binary Crossentropy |
| Evaluation Metric | Accuracy |
| Maximum Epochs | 20 |

---

## 🛡️ Training Callbacks

| Callback | Purpose |
|---|---|
| **EarlyStopping** | Stops training when validation performance plateaus and restores the best model weights. |
| **ModelCheckpoint** | Saves the best performing model during training. |
| **ReduceLROnPlateau** | Reduces the learning rate when validation performance stops improving. |

---

## 🔮 Prediction Pipeline

1. User uploads a `.jpg`, `.jpeg`, or `.png` image.
2. The image is converted to RGB.
3. The image is resized to **224 × 224**.
4. The image is passed through the trained ResNet50 model.
5. The model generates a prediction probability.
6. The probability is converted into a **Cat** or **Dog** label.
7. The Streamlit app displays:
   - ✅ Predicted class
   - 📊 Prediction confidence
   - 🖼️ Uploaded image preview

---

## 📁 Repository Structure

```text
CNN_project/
│
├── app.py                 # Streamlit application entry point
├── best_model.keras        # Trained model (tracked via Git LFS)
├── requirements.txt        # Project dependencies
├── README.md                # Project documentation
│
└── src/
    ├── callbacks.py         # Training callbacks (EarlyStopping, Checkpoint, etc.)
    ├── check_data.py        # Dataset validation & corrupted image handling
    ├── data_loader.py       # Data loading & augmentation pipeline
    ├── model.py             # Model architecture definition
    └── train.py             # Training script
```

---

## 🚀 Getting Started

```bash
# Clone the repository
git clone https://github.com/<your-username>/CNN_project.git
cd CNN_project

# Pull LFS-tracked files (e.g. best_model.keras)
git lfs pull

# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

---

## 🗺️ Roadmap

- [ ] Add model performance visualizations (accuracy/loss curves)
- [ ] Add confusion matrix & classification report
- [ ] Support batch image predictions
- [ ] Add Docker support for deployment
- [ ] Experiment with other backbones (EfficientNet, MobileNet)

---

## 👤 Author

**Abhash**
IIT Bhubaneswar

---

<div align="center">

Made with ❤️ using TensorFlow & Streamlit

</div>

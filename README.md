# 🐱🐶 Cat vs Dog Image Classifier

A deep learning image classification project that predicts whether an uploaded image is a Cat or a Dog using a ResNet50-based transfer learning model.

## 🚀 Live Demo

Streamlit App: cnn_project ∙ main ∙ app.py

## 📌 Project Overview

This project uses transfer learning with ResNet50 for binary image classification.

The application allows users to upload a cat or dog image and displays:

- 🐱 Cat or 🐶 Dog prediction
- 📊 Prediction confidence
- 🖼️ Uploaded image preview

## 🧠 Model

- Architecture: ResNet50
- Input Size: 224 × 224 × 3
- Task: Binary Image Classification
- Classes: Cat and Dog
- Transfer Learning: Yes

## 📊 Dataset

The dataset contains approximately:

- Cat images: 12,497
- Dog images: 12,494

During preprocessing, corrupted JPEG files were detected and handled.

## 🛠️ Technologies Used

- Python
- TensorFlow
- Keras
- ResNet50
- NumPy
- Pillow
- Streamlit
- Git
- GitHub
- Git LFS

## 📁 Project Structure

CNN_project/
│
├── app.py
├── best_model.keras
├── requirements.txt
├── README.md
│
└── src/
    ├── data_loader.py
    ├── model.py
    └── train.py

## ⚙️ Installation

```bash
pip install -r requirements.txt

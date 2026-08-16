import os

import numpy as np
import streamlit as st
import tensorflow as tf
from PIL import Image
from tensorflow.keras.applications.resnet50 import preprocess_input


MODEL_PATH = "best_model.keras"


@st.cache_resource
def load_model():
    model = tf.keras.models.load_model(MODEL_PATH, safe_mode=False)

    # The currently trained artifact contains an anonymous Lambda that
    # references preprocess_input. Replace it with the known function after loading.
    for layer in model.layers:
        if isinstance(layer, tf.keras.layers.Lambda):
            layer.function = preprocess_input

    return model


st.set_page_config(page_title="Cat vs Dog Classifier", page_icon="🐱")
st.title("🐱 Cat vs Dog Classifier")
st.write("Upload an image and the trained ResNet50 model will classify it.")

if not os.path.exists(MODEL_PATH):
    st.error(f"Model file not found: {MODEL_PATH}")
    st.stop()

model = load_model()

uploaded_file = st.file_uploader("Upload a cat or dog image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded image", use_container_width=True)

    image_array = np.array(image.resize((224, 224)), dtype=np.float32)
    image_array = np.expand_dims(image_array, axis=0)

    prediction = float(model.predict(image_array, verbose=0)[0][0])

    if prediction >= 0.5:
        label = "Dog"
        confidence = prediction
    else:
        label = "Cat"
        confidence = 1.0 - prediction

    st.subheader(f"Prediction: {label}")
    st.metric("Confidence", f"{confidence * 100:.2f}%")

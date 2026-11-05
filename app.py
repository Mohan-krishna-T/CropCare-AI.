import streamlit as st
from PIL import Image

st.title("CropCare AI")
st.write("Upload a crop leaf image to begin.")

uploaded_file = st.file_uploader(
    "Choose a leaf image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded leaf", use_container_width=True)

import streamlit as st
import pytesseract
from PIL import Image
st.title("OCR - Optical Character Recognition")
img = st.sidebar.file_uploader("Choose an image")
if img is not None:
  img_read = Image.open(img)
  st.image(img,caption='Uploaded Image')
  if st.button('PREDICT'):
    op = pytesseract.image_to_string(img_read)
    st.write(op)

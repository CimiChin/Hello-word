import streamlit as st
from PIL import Image

st.title("Naruto vs Sasuke")
st.write("Pertarungan legendaris antara dua ninja hebat!")

# Tampilkan gambar
image = Image.open("images/naruto_vs_sasuke.jpg")
st.image(image, caption="Naruto vs Sasuke", use_column_width=True)

st.markdown("Siapa jagoan kamu? 🤜🤛")

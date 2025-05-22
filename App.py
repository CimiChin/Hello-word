import streamlit as st
import random

# Inisialisasi angka jika belum ada di session_state
if 'target' not in st.session_state:
    st.session_state.target = random.randint(1, 10)

st.title("🎲 Game Tebak Angka")
st.write("Tebak angka antara 1 sampai 10")

guess = st.number_input("Masukkan tebakan kamu:", min_value=1, max_value=10, step=1)

if st.button("Tebak"):
    if guess == st.session_state.target:
        st.success("🎉 Benar! Kamu berhasil menebak angkanya!")
        st.balloons()
        # Reset angka
        st.session_state.target = random.randint(1, 10)
    else:
        st.error("❌ Salah. Coba lagi!")

if st.button("Reset Game"):
    st.session_state.target = random.randint(1, 10)
    st.info("Game telah di-reset.")

import streamlit as st

def show():
    st.title("📸 Galeria do Trabalho")
    st.write("Veja abaixo algumas imagens do trabalho feito para a feira:")
    st.image("img/criando_1.jpg", caption="Diorama 1: João e o Pé de Feijão")
    st.image("img/criando_pedro.jpg", caption="Diorama 2: Vista Lateral")
    st.image("img/pronto_sf.png", caption="Detalhes do Castelo")
    st.image("img/pronto_1.jpg", caption="Detalhes do Castelo")
    st.image("img/pronto_2.jpg", caption="Detalhes do Castelo")
    st.image("img/pronto_3.jpg", caption="Detalhes do Castelo")

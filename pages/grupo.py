import streamlit as st
from PIL import Image

def resize_image(image_path, max_height=200):
    """
    Redimensiona a imagem para uma altura máxima, mantendo a proporção.
    """
    image = Image.open(image_path)
    width, height = image.size
    new_height = max_height
    new_width = int((new_height / height) * width)
    image = image.resize((new_width, new_height))  # Redimensiona mantendo a proporção
    return image

def show():
    st.title("👥 O Grupo")
    st.write("""
    Conheça os integrantes do grupo e a professora Gislene. 
    Este projeto foi desenvolvido por alunos do **5º ano do Ensino Fundamental** da **Escola Estadual de Mucuri**. 

    O trabalho faz parte da **Feira de Ciências, Cultura e Empreendedorismo**, onde cada grupo tem a missão de criar algo especial, utilizando criatividade, trabalho em equipe e dedicação. Nosso tema é baseado na história de **João e o Pé de Feijão**, que foi transformada em uma apresentação educativa e interativa.

    Acompanhe os talentos por trás desse incrível projeto!
    """)

    # Dados dos alunos
    members = [
        {"name": "Pedro", "img": "img/pedro1.png"},
        {"name": "Rodrigo", "img": "img/rodrigo1.png"},
        {"name": "Rafael", "img": "img/Rafael1.png"},
        {"name": "Yong", "img": "img/yong1.png"},
        {"name": "Pietro", "img": "img/pietro1.png"},
        {"name": "Tia Gislene", "img": "img/professora.jpg"},
    ]

    # Exibir todas as imagens redimensionadas em colunas
    st.write("### Integrantes do Grupo")
    cols = st.columns(3)  # Configurando 3 colunas para layout

    for index, member in enumerate(members):
        with cols[index % 3]:  # Distribuir imagens entre as colunas
            resized_image = resize_image(member["img"], max_height=200)
            st.image(resized_image, caption=member["name"], use_container_width=False)  # Exibir imagens redimensionadas

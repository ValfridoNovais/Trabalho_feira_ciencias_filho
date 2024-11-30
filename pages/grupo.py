import streamlit as st
from PIL import Image

def resize_image(image_path, max_height=200):
    """
    Redimensiona a imagem para uma altura máxima, mantendo a proporção.
    """
    image = Image.open(image_path)
    # Define as dimensões máximas (altura fixa, largura proporcional)
    width, height = image.size
    new_height = max_height
    new_width = int((new_height / height) * width)
    image = image.resize((new_width, new_height))  # Sem o argumento ANTIALIAS
    return image

def show():
    st.title("👥 O Grupo")
    st.write("""
    Conheça os integrantes do grupo e a professora Luciana. 
    Este projeto foi desenvolvido por alunos do **5º ano do Ensino Fundamental** da **Escola Estadual de Mucuri**. 

    O trabalho faz parte da **Feira de Ciências, Cultura e Empreendedorismo**, onde cada grupo tem a missão de criar algo especial, utilizando criatividade, trabalho em equipe e dedicação. Nosso tema é baseado na história de **João e o Pé de Feijão**, que foi transformada em uma apresentação educativa e interativa.

    Acompanhe os talentos por trás desse incrível projeto!
    """)


    # Dados dos alunos
    members = [
        {"name": "Pedro", "img": "img/pedro1.png"},
        {"name": "Rodrigo", "img": "img/rodrigo1.png"},
        {"name": "Rafael", "img": "img/rafael1.png"},
        {"name": "Yong", "img": "img/yong1.png"},
        {"name": "Pietro", "img": "img/pietro1.png"},
        {"name": "Tia Luciana", "img": "img/professora.jpg"},
    ]

    # Configurando as colunas
    col1, col2 = st.columns([1, 3])  # Coluna 1 = 25%, Coluna 2 = 75%

    # Parte Esquerda: Miniaturas
    with col1:
        st.write("### Miniaturas")
        selected_name = st.radio(
            "Selecione um membro:",
            [member["name"] for member in members],  # Nomes como opções
            index=0  # Pré-selecionar o primeiro membro
        )

    # Parte Direita: Imagem Ampliada
    with col2:
        st.write("### Imagem Selecionada")
        # Encontrar o membro selecionado
        selected_member = next(member for member in members if member["name"] == selected_name)

        # Redimensionar a imagem selecionada
        resized_image = resize_image(selected_member["img"], max_height=200)
        
        # Mostrar a imagem redimensionada
        st.image(resized_image, caption=selected_member["name"], use_container_width=False)

  
        


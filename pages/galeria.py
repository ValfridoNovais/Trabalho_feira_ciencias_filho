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
    return image.resize((new_width, new_height))

def rotate_image(image, angle):
    """
    Rotaciona uma imagem já carregada em um ângulo especificado.
    """
    return image.rotate(angle, expand=True)

def show():
    st.title("📸 Galeria do Trabalho")
    st.write("Veja abaixo algumas imagens do trabalho feito para a feira:")

    # Lista de imagens com opções de rotação
    images = [
        {"path": "img/criando_1.jpg", "caption": "Mãe Thaíse auxiliando os alunos Pedro, Rodrigo e Rafael em um dos encontros pro desenvolvimento", "rotate": 0},
        {"path": "img/criando_pedro.jpg", "caption": "Pedro perparando uma das folhas do pé de feijão", "rotate": 0},
        {"path": "img/castelo.jpg", "caption": "Detalhes do Castelo pronto, com todos os detalhes ", "rotate": 0},
        {"path": "img/pronto_1.jpg", "caption": "Uma vista da Maquete", "rotate": 90},
        {"path": "img/Estrutura.png", "caption": "Detalhes do Castelo junto com a base em fase de modelagem", "rotate": 0},
        {"path": "img/pronto_3.jpg", "caption": "Maquete pronta", "rotate": 90},
    ]

    # Renderizar as imagens
    for img in images:
        # Redimensionar a imagem
        resized_image = resize_image(img["path"], max_height=200)
        
        # Rotacionar se necessário
        if img["rotate"] != 0:
            resized_image = rotate_image(resized_image, img["rotate"])
        
        # Exibir a imagem
        st.image(resized_image, caption=img["caption"], use_container_width=False)

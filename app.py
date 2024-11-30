import streamlit as st
from streamlit_option_menu import option_menu

# Configuração inicial do site
st.set_page_config(page_title="João e o Pé de Feijão", layout="wide")

# Menu Superior
selected = option_menu(
    menu_title=None,  # Oculta o título do menu
    options=["O Grupo", "A História", "Galeria", "Curiosidades", "Quiz"],  # Opções do menu
    icons=["people", "book", "camera", "star", "puzzle"],  # Ícones correspondentes
    menu_icon="cast",  # Ícone geral do menu
    default_index=0,  # Abre na primeira opção por padrão
    orientation="horizontal",  # Define o menu como horizontal
    styles={
        "container": {"background-color": "#4CAF50", "padding": "5px"},
        "nav-link": {"font-size": "16px", "text-align": "center", "color": "white"},
        "nav-link-selected": {"background-color": "#45a049"},
    },
)

# Conteúdo baseado na seleção do menu
if selected == "O Grupo":
    st.title("🏫 O Grupo")
    st.header("Bem-vindo à Feira de Ciências!")
    st.write("""
    Este site foi criado para apresentar o trabalho da feira de ciências baseado na história de **João e o Pé de Feijão**. 
    Explore para aprender mais sobre essa incrível história!
    """)
    st.write("""
    Nosso grupo é composto por alunos criativos e dedicados que trabalharam para trazer essa incrível história à vida!
    """)

elif selected == "A História":
    st.title("📖 A História")
    st.write("""
    João era um menino que trocou sua vaca por alguns feijões mágicos. Quando ele plantou os feijões, cresceu um enorme pé de feijão que alcançava as nuvens.
    No topo, ele encontrou um castelo, um gigante e muitos tesouros, incluindo uma harpa dourada e uma galinha que botava ovos de ouro. 
    A história nos ensina sobre coragem e inteligência!
    """)

elif selected == "Galeria":
    st.title("📸 Galeria do Trabalho")
    st.write("Veja abaixo algumas imagens do trabalho feito para a feira:")
    # Carregando as imagens da pasta 'img'
    st.image("img/criando_1.jpg", caption="Diorama 1: João e o Pé de Feijão")
    st.image("img/criando_pedro.jpg", caption="Diorama 2: Vista Lateral")
    st.image("img/pronto_sf.png", caption="Detalhes do Castelo")
    st.image("img/pronto_1.jpg", caption="Detalhes do Castelo")
    st.image("img/pronto_2.jpg", caption="Detalhes do Castelo")
    st.image("img/pronto_3.jpg", caption="Detalhes do Castelo")

elif selected == "Curiosidades":
    st.title("🌟 Curiosidades")
    st.write("""
    - A história de João e o Pé de Feijão é um conto de fadas clássico originado na Inglaterra.
    - A primeira versão escrita apareceu no século XIX.
    - Representa a luta entre o bem (João) e o mal (Gigante), mostrando que inteligência é mais importante do que força.
    """)

elif selected == "Quiz":
    st.title("🎮 Quiz Interativo")
    st.write("Teste seus conhecimentos sobre a história:")
    quiz = st.radio("O que João encontrou no castelo?", 
                    ["Um dragão", "Uma galinha que bota ovos de ouro", "Um baú vazio"])
    if quiz == "Uma galinha que bota ovos de ouro":
        st.success("Isso mesmo! João encontrou a galinha mágica.")
    else:
        st.error("Resposta errada. Tente novamente!")

# Rodapé
st.write("---")
st.write("Feito com ❤️ por Valfrido Novais e Thaíse Novais e apresentado por Pedro Novais, Rodrigo Novais, Yang.")

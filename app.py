import streamlit as st
from streamlit_option_menu import option_menu
from pages import grupo, historia, galeria, curiosidades, quiz

# Configuração inicial
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

# Renderizar a seção correspondente
if selected == "O Grupo":
    grupo.show()
elif selected == "A História":
    historia.show()
elif selected == "Galeria":
    galeria.show()
elif selected == "Curiosidades":
    curiosidades.show()
elif selected == "Quiz":
    quiz.show()

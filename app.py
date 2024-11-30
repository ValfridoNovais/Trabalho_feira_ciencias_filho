import streamlit as st
from streamlit_option_menu import option_menu
from pages import grupo, historia, galeria, curiosidades, quiz

# Configuração inicial
st.set_page_config(page_title="João e o Pé de Feijão", layout="wide")

# CSS para organizar o menu no celular
st.markdown(
    """
    <style>
    /* Remove a margem da barra lateral */
    [data-testid="stSidebar"] {
        display: none;
    }
    [data-testid="stAppViewContainer"] {
        margin-left: 0;
    }

    /* Ajuste dos ícones acima do texto */
    .css-1y4p8pa.e1fqkh3o3 > div {
        display: flex;
        flex-direction: column; /* Ícone em cima do texto */
        align-items: center;    /* Centraliza os itens */
        font-size: 12px;        /* Reduz o tamanho do texto */
    }

    /* Responsividade no celular */
    @media screen and (max-width: 768px) {
        .css-1y4p8pa.e1fqkh3o3 {
            justify-content: space-around; /* Espaçamento uniforme entre itens */
        }
        .css-1y4p8pa.e1fqkh3o3 > div {
            font-size: 10px; /* Reduz ainda mais o texto no celular */
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

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
        "nav-link": {"font-size": "14px", "text-align": "center", "color": "white"},
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

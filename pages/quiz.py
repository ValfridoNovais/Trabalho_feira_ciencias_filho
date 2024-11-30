import streamlit as st

def show():
    st.title("🎮 Quiz Interativo")
    st.write("Teste seus conhecimentos sobre a história:")
    quiz = st.radio("O que João encontrou no castelo?", 
                    ["Um dragão", "Uma galinha que bota ovos de ouro", "Um baú vazio"])
    if quiz == "Uma galinha que bota ovos de ouro":
        st.success("Isso mesmo! João encontrou a galinha mágica.")
    else:
        st.error("Resposta errada. Tente novamente!")

import streamlit as st
import random

def show():
    # Título
    st.title("🎮 Quiz Interativo")
    st.write("Teste seus conhecimentos sobre a história de João e o Pé de Feijão!")

    # Inicializando estados na sessão
    if "score" not in st.session_state:
        st.session_state.score = 0  # Pontuação inicial
    if "question_index" not in st.session_state:
        st.session_state.question_index = 0  # Índice da questão atual
    if "stop_quiz" not in st.session_state:
        st.session_state.stop_quiz = False  # Controle para parar o quiz
    if "answered" not in st.session_state:
        st.session_state.answered = False  # Controle de resposta por questão
    if "shuffled_questions" not in st.session_state:
        st.session_state.shuffled_questions = []  # Perguntas embaralhadas

    # Lista original de perguntas
    questions = [
        {"question": "O que João trocou pela vaca?", "options": ["Alguns feijões mágicos"], "answer": "Alguns feijões mágicos", "points": 2},
        {"question": "O que cresceu dos feijões mágicos?", "options": ["Um pé de feijão gigante"], "answer": "Um pé de feijão gigante", "points": 2},
        {"question": "Quem vivia no castelo?", "options": ["Um gigante"], "answer": "Um gigante", "points": 2},
        {"question": "Por que João aceitou os feijões mágicos em troca da vaca?", "options": ["Porque ele era curioso e impulsivo"], "answer": "Porque ele era curioso e impulsivo", "points": 3},
        {"question": "Como João escapou do gigante?", "options": ["Cortou o pé de feijão"], "answer": "Cortou o pé de feijão", "points": 3},
        {"question": "O que a decisão de João de trocar a vaca por feijões mágicos nos ensina?", "options": ["A importância de arriscar às vezes"], "answer": "A importância de arriscar às vezes", "points": 4},
        {"question": "Qual é a mensagem principal da história?", "options": ["Inteligência pode superar a força"], "answer": "Inteligência pode superar a força", "points": 4},
        {"question": "Por que João dividiu a riqueza com sua mãe?", "options": ["Porque cuidar da família é importante"], "answer": "Porque cuidar da família é importante", "points": 4},
    ]

    # Opções fictícias para preencher as perguntas
    filler_options = [
        "Uma galinha dourada", "Um baú de ouro", "Um castelo mágico",
        "Uma harpa mágica", "Uma árvore de maçãs", "Que dinheiro é mais importante",
        "Porque ele queria enganar o gigante","Uma bolsa cheia de moedas", "Uma espada mágica", "Um mapa do tesouro", "Uma coroa dourada", "Um anel encantado", "Uma árvore de feijões mágicos", "Uma torre de cristal", "Uma varinha mágica", "Uma poção de invisibilidade", "Um livro de feitiços", "Um dragão adormecido", "Uma ponte para o céu", "Uma carruagem encantada", "Uma bola de cristal", "Uma flauta mágica", "Um cavalo voador", "Uma chave dourada", "Uma caverna cheia de diamantes", "Uma pulseira mágica", "Um relógio que para o tempo", "Ganância e poder", "A força física", "Os perigos da curiosidade"
        ]
    

    # Função para embaralhar perguntas e respostas
    def shuffle_questions():
        shuffled = []
        for question in questions:
            # Adicionar opções fictícias até completar 4
            while len(question["options"]) < 4:
                option = random.choice(filler_options)
                if option not in question["options"] and option != question["answer"]:
                    question["options"].append(option)
            # Embaralhar as opções
            random.shuffle(question["options"])
            shuffled.append(question)
        random.shuffle(shuffled)
        return shuffled

    # Inicializar as perguntas embaralhadas ao carregar o quiz
    if not st.session_state.shuffled_questions:
        st.session_state.shuffled_questions = shuffle_questions()

    # Função para reiniciar o quiz
    def reset_quiz():
        st.session_state.score = 0
        st.session_state.question_index = 0
        st.session_state.stop_quiz = False
        st.session_state.answered = False
        st.session_state.shuffled_questions = shuffle_questions()  # Reembaralha as perguntas

    # Verifica se o quiz foi interrompido
    if st.session_state.stop_quiz:
        st.success(f"Você decidiu parar! Sua pontuação final é: {st.session_state.score}")
        if st.button("Reiniciar Quiz"):
            reset_quiz()  # Reinicia o quiz no fluxo natural
        return

    # Pegar a questão atual
    current_question = st.session_state.shuffled_questions[st.session_state.question_index]

    # Exibir a pergunta
    st.subheader(f"Questão {st.session_state.question_index + 1}: {current_question['question']}")
    selected_option = st.radio(
        "Escolha uma opção:",
        current_question["options"],
        key=f"q{st.session_state.question_index}"
    )

    # Botões para enviar ou parar
    col1, col2 = st.columns(2)

    with col1:
        if st.button("Enviar Resposta") and not st.session_state.answered:
            st.session_state.answered = True
            if selected_option == current_question["answer"]:
                st.session_state.score += current_question["points"]
                st.success(f"Correto! Você ganhou {current_question['points']} pontos.")
            else:
                st.session_state.score -= 1
                st.error(f"Errado! Você perdeu 1 ponto. A resposta correta era: {current_question['answer']}")

    with col2:
        if st.button("Parar o Quiz"):
            st.session_state.stop_quiz = True

    # Exibir o botão para próxima questão
    if st.session_state.answered:
        if st.button("Próxima Questão"):
            # Avançar para a próxima questão
            if st.session_state.question_index + 1 < len(st.session_state.shuffled_questions):
                st.session_state.question_index += 1
                st.session_state.answered = False
            else:
                st.success(f"Parabéns! Você completou o quiz. Sua pontuação final é: {st.session_state.score}")
                st.session_state.stop_quiz = True





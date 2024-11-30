from PIL import Image, ImageDraw, ImageFont

def create_folder():
    # Configurações básicas
    largura, altura = 1080, 1920
    fundo = (255, 255, 255)  # Cor branca

    # Criar imagem base
    img = Image.new("RGB", (largura, altura), fundo)
    draw = ImageDraw.Draw(img)

    # Fontes (certifique-se de que os caminhos das fontes estejam corretos)
    font_title = ImageFont.truetype("arial.ttf", 80)
    font_subtitle = ImageFont.truetype("arial.ttf", 50)
    font_body = ImageFont.truetype("arial.ttf", 40)

    # Título
    draw.text((40, 50), "Escola Estadual de Mucuri", font=font_title, fill=(0, 0, 0))
    draw.text((40, 150), "Feira de Ciências, Cultura e Empreendedorismo", font=font_subtitle, fill=(0, 0, 0))

    # Tema
    draw.text((40, 250), "Tema: João e o Pé de Feijão", font=font_subtitle, fill=(0, 100, 0))

    # Nomes dos alunos e professora
    alunos = [
        "Pedro", "Rodrigo", "Rafael", "Yong", "Iure", "Pietro"
    ]
    draw.text((40, 350), "Alunos:", font=font_body, fill=(0, 0, 0))
    for i, aluno in enumerate(alunos):
        draw.text((60, 400 + i * 40), f"- {aluno}", font=font_body, fill=(0, 0, 0))
    draw.text((40, 700), "Professora: Gislene", font=font_body, fill=(0, 0, 0))

    # QR Code
    qr_code_path = "C:/Repositorios_GitHube/MeusProjetos/Trabalho_feira_ciencias_filho/img/qrcode.jpg"
    qr_code = Image.open(qr_code_path)  # Carregando o QR Code
    qr_code = qr_code.resize((300, 300))  # Redimensiona o QR Code
    img.paste(qr_code, (40, 800))  # Coloca o QR Code na imagem base

    # Descrição do Quiz
    quiz_text = (
        "No site, participe do nosso Quiz interativo!\n"
        "As 15 primeiras pessoas que acertarem todas as questões\n"
        "ganharão um brinde exclusivo! Escaneie o QR Code para participar."
    )
    draw.text((40, 1150), quiz_text, font=font_body, fill=(0, 0, 0))

    # Imagem Temática
    tema_img_path = "C:/Repositorios_GitHube/MeusProjetos/Trabalho_feira_ciencias_filho/img/joao_pe_de_feijao.png"
    tema_img = Image.open(tema_img_path)  # Carregando a imagem temática
    tema_img = tema_img.resize((600, 400))  # Redimensiona a imagem temática
    img.paste(tema_img, (400, 800))  # Coloca a imagem temática na base

    # Salvar o folder
    img.save("folder_trabalho_feira.png")  # Salva o folder final no diretório do projeto

# Chamar a função para criar o folder
create_folder()


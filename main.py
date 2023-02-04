import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os

# Coletando nomes e e-mails da planilha
pessoas = pd.read_excel(r"Ouvintes.xlsx")
emails = (pessoas['Email'].values)
nomes = (pessoas['Nome'].values)

# definir o modelo do certificado e as fontes que serão utlizadas
modelo_certificado = Image.open('certificado.png')
fonte = ImageFont.truetype("font/DancingScript-Regular.ttf", 60)

sender_email = "seuemail@seuemail.com"
password = "sua_senha"

# SMTP do provedor desejado
server = smtplib.SMTP('smtp-mail.outlook.com', 587)

server.ehlo()
server.starttls()
server.login(sender_email, password)

for i, nome in enumerate(nomes):
    # Criar uma cópia da imagem original para cada nome
    imagem = modelo_certificado.copy()

    # Desenhar o texto na imagem
    desenho = ImageDraw.Draw(imagem)
    desenho.text((616, 590), nome, font=fonte, fill=('black'))

    # Salvar a imagem com o nome do destinatário na pasta certificados
    imagem.save(f"certificados/certificado_{nome}.png")

    # Enviar Email
    receiver_email = emails[i]
    message = MIMEMultipart()
    message["Subject"] = "Seu certificado de participação"
    message["From"] = sender_email
    message["To"] = receiver_email

    with open(f"certificados/certificado_{nome}.png", "rb") as f:
        img_data = f.read()
        image = MIMEImage(img_data)
        message.attach(image)

    text = MIMEText("Parabéns, você recebeu um certificado de participação!")
    message.attach(text)

    server.send_message(message)

server.quit()

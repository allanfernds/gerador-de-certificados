from PIL import Image, ImageDraw, ImageFont
import pandas as pd


pessoas = pd.read_excel(r"Ouvintes.xlsx", skiprows=[0])
nomes = (pessoas['Nome'].values)

# definir o modelo do certificado e as fontes que serão utlizadas
modelo_certificado = Image.open('certificado.png')
fonte = ImageFont.truetype("font/DancingScript-Regular.ttf", 60)

for nome in nomes:
    # Criar uma cópia da imagem original para cada nome
    imagem = modelo_certificado.copy()

    # Desenhar o texto na imagem
    desenho = ImageDraw.Draw(imagem)
    desenho.text((616, 590), nome, font=fonte, fill=('black'))

    # Salvar a imagem com o nome do destinatário na pasta certificados
    imagem.save(f"certificados/certificado_{nome}.png")

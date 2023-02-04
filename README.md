
# Gerador de Certificados

Esse é um script em Python que lê uma planilha de Excel com a lista de nomes de destinatários de certificados e gera imagens de certificados personalizadas para cada um deles.


## Requisitos
- Python 3
- Biblioteca smtplib
- Biblioteca PIL (Pillow)
- Biblioteca Pandas
- Modelo de Certificado em formato PNG
- Fonte para o texto do certificado (O projeto já possui uma font de exemplo na pasta font)

## Funcionamento

Este script em Python lê nomes de uma planilha Excel, cria cópias personalizadas do modelo de certificado com cada nome usando a biblioteca PIL, salva as imagens na pasta "certificados" e, finalmente, envia cada certificado por e-mail aos destinatários. O envio de e-mail é realizado através das bibliotecas SMTPLib, MIMEMultipart e PIL, usando seu endereço de e-mail e senha para conectar ao servidor de e-mail.

## Como usar

1. Instale as bibliotecas necessárias:

    ```
    pip install Pillow pandas
    ```
2. Insira sua lista de destinatários no arquivo Excel "Ouvintes.xlsx" (Deve possuir duas colunas, Nome e Email).
3. Adicione o modelo de certificado em formato PNG.
4. Adicione seu Email e Senha nas linhas 18 e 19,
5. Configure o SMTP do seu provedor de email (ja está configurado para usar o Outlook)
6. Adicione a fonte para o texto do certificado na pasta "font".(opcional)
7. Execute o script:

    ```
    python gerador_certificados.py
    ```


## Contribuições
Contribuições são sempre bem-vindas! Sinta-se livre para abrir uma issue ou fazer uma pull request.

## Notas
Não esqueça de verificar se o caminho para o arquivo de destinatários, o modelo de certificado e a fonte estão corretos no código.



# Gerador de Certificados

Esse é um script em Python que lê uma planilha de Excel com a lista de nomes de destinatários de certificados e gera imagens de certificados personalizadas para cada um deles.


## Requisitos
- Python 3
- Biblioteca PIL (Pillow)
- Biblioteca Pandas
- Modelo de Certificado em formato PNG
- Fonte para o texto do certificado (O projeto já possui uma font de exemplo na pasta font)

## Funcionamento

O script lê os nomes a partir de um arquivo Excel (formato .xlsx) e, em seguida, cria uma cópia do modelo de certificado para cada nome na lista. O nome de cada destinatário é escrito na imagem do certificado utilizando a biblioteca PIL (Pillow). Por fim, as imagens são salvas em uma pasta com o nome de "certificados" e o nome de cada pessoa como sufixo.

## Como usar

1. Instale as bibliotecas necessárias:

    ```
    pip install Pillow pandas
    ```
2. Insira sua lista de destinatários no arquivo Excel "Ouvintes.xlsx".
3. Adicione o modelo de certificado em formato PNG.
4. Adicione a fonte para o texto do certificado na pasta "font".(opcional)
5. Execute o script:

    ```
    python gerador_certificados.py
    ```


## Contribuições
Contribuições são sempre bem-vindas! Sinta-se livre para abrir uma issue ou fazer uma pull request.

## Notas
Não esqueça de verificar se o caminho para o arquivo de destinatários, o modelo de certificado e a fonte estão corretos no código.


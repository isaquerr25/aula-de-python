# Abrir o arquivo original para leitura
with open("texto.txt", "r",encoding="utf-8") as arquivo_origem:
    # Ler o conteúdo do arquivo
    texto = arquivo_origem.read()

# Substituir a palavra "cachorro" por "cão"
texto_modificado = texto.replace("cachorro", "cão")

# Abrir um novo arquivo para escrever o texto modificado
with open("texto_modificado.txt", "w",encoding="utf-8") as arquivo_destino:
    # Escrever o texto modificado no novo arquivo
    arquivo_destino.write(texto_modificado)

print("Substituição concluída. Verifique o arquivo 'texto_modificado.txt'.")

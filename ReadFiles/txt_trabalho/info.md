---
runme:
  id: 01HT14H8J7347JKFXJ5T1Y7QES
  version: v3
---

Neste exemplo, vamos ler um arquivo de texto, substituir todas as ocorrências de uma palavra específica por outra e salvar o resultado em um novo arquivo.

Suponha que temos um arquivo chamado "texto.txt" com o seguinte conteúdo:

O cachorro pulou sobre o gato.
Vamos substituir todas as ocorrências da palavra "cachorro" por "cão". Aqui está o código Python para realizar isso:

# Abrir o arquivo original para leitura

```sh {"id":"01HT14HR87Y6E4A0Y0X5T8J0Q0"}
# Abrir o arquivo original para leitura
with open("texto.txt", "r",encoding="utf-8") as arquivo_origem:
    # Ler o conteúdo do arquivo
    texto = arquivo_origem.read()

# Substituir a palavra "cachorro" por "cão"
texto_modificado = texto.replace("cachorro", "cão")

# Abrir um novo arquivo para escrever o texto modificado
with open("texto_modificado.txt", "w", encoding="utf-8") as arquivo_destino:
    # Escrever o texto modificado no novo arquivo
    arquivo_destino.write(texto_modificado)

print("Substituição concluída. Verifique o arquivo 'texto_modificado.txt'.")

```

# Substituir a palavra "cachorro" por "cão"

```sh {"id":"01HT14HXMVFAVEJ85ZWBS1GD0V"}
texto_modificado = texto.replace("cachorro", "cão")
```

Depois de executar esse código, o arquivo "texto_modificado.txt" conterá o seguinte conteúdo:

```sh {"id":"01HT14K6DXD0KGM1FFSZC4Y7WV"}
O cão pulou sobre o gato.
```

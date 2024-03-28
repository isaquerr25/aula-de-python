# Lista de palavras
palavras = ["banana", "abacaxi", "uva", "laranja", "abóbora", "maçã"]

# Função para verificar se uma palavra começa com "a"
def comeca_com_a(palavra):
    return palavra.startswith("a")

# Filtrar a lista de palavras para obter apenas aquelas que começam com "a"
palavras_com_a = list(filter(comeca_com_a, palavras))

# Exibir a lista de palavras filtradas
print("Palavras que começam com 'a':", palavras_com_a)

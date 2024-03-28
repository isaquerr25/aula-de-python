# Filtrar uma lista de números para obter apenas os números pares:

# Lista de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Função para verificar se um número é par
# "%"" faz o calculo do modulo do funçâo
def eh_par(numero):
  return numero % 2 == 0

# Filtrar a lista de números para obter apenas os números pares
numeros_pares = list(filter(eh_par, numeros))

# Exibir a lista de números pares
print("Números pares:", numeros_pares)

# Números pares: [2, 4, 6, 8, 10]

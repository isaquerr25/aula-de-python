# Solicita ao usuário que insira um número
numero = float(input("Digite um número: "))

# Verifica se o número é maior que 50
if numero > 50:
    print("O número é maior que 50.")
# Verifica se o número é menor que 50
elif numero < 50:
    print("O número é menor que 50.")
# Se não for maior nem menor, então é igual a 50
else:
    print("O número é igual a 50.")

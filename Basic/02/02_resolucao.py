"""
  Exercício: Calculadora de Média

  Crie um programa em Python que solicite ao usuário que insira três notas (N1, N2 e N3). Em seguida, o 
  programa deve calcular e exibir a média dessas notas.

  Dica: A média é calculada somando todas as notas e dividindo pelo número total de notas.

"""
  
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Calcula a média das notas
media = (nota1 + nota2 + nota3) / 3

# Exibe a média
print("A média das notas é:", media)
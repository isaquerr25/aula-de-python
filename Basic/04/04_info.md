---
runme:
  id: 01HT136XGNFMYXN1S2H0E34KBJ
  version: v3
---

Tipos de Loops em Python
Existem dois tipos principais de loops em Python:

Loop while: Executa um bloco de código enquanto uma condição especificada for verdadeira.

Loop for: Itera sobre um sequência (como uma lista, tupla, string, etc.) e executa um bloco de código para cada item na sequência.

Loop while
O loop "while" continua a executar seu bloco de código enquanto a condição especificada for verdadeira. A condição é verificada antes de cada iteração do loop.

# Exemplo de loop while

```sh {"id":"01HT137XN3QY8DAS6RPDM60MYV"}
contador = 0
while contador < 5:
  print("O contador é:", contador)
  contador += 1

O contador é: 0
O contador é: 1
O contador é: 2
O contador é: 3
O contador é: 4

```

# Exemplo de loop for

```sh {"id":"01HT137C2DDFD8377GVKGYWVDC"}
frutas = ["maçã", "banana", "laranja"]
for fruta in frutas:
  print("Eu gosto de", fruta)

Eu gosto de maçã
Eu gosto de banana
Eu gosto de laranja

```

```sh {"id":"01HT1398TRHBGND89WY1KGC7WN"}
# Exemplo de loop for comum usando i
for i in range(5):  # range(5) gera uma sequência de 0 a 4
  print("O valor de i é:", i)

O valor de i é: 0
O valor de i é: 1
O valor de i é: 2
O valor de i é: 3
O valor de i é: 4

```

```sh {"id":"01HT13A7XJXYWNPZZY2Y2KRAMP"}
# Exemplo de loop for com len()
frutas = ["maçã", "banana", "laranja", "uva"]

# Itera sobre a lista de frutas usando len() para obter o comprimento da lista
for i in range(len(frutas)):
    print("Na posição", i, "temos a fruta", frutas[i])


Na posição 0 temos a fruta maçã
Na posição 1 temos a fruta banana
Na posição 2 temos a fruta laranja
Na posição 3 temos a fruta uva

```
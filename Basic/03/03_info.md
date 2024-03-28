---
runme:
  id: 01HT12NMZAMFJN9SW2ET4R338X
  version: v3
---

Tipos de Condicionais em Python
As condicionais em Python permitem que o seu programa tome decisões com base em certas condições. Existem três tipos principais de condicionais em Python:

if: O bloco de código dentro de um "if" é executado apenas se a condição especificada for verdadeira.

elif (abreviação de "else if"): O bloco de código dentro de um "elif" é executado se a condição do "if" anterior for falsa e a condição especificada no "elif" for verdadeira.

else: O bloco de código dentro de um "else" é executado se nenhuma das condições anteriores for verdadeira.

Exemplo Prático
Vamos ver um exemplo prático que ilustra o uso desses tipos de condicionais:

# Exemplo de condicionais em Python

idade = 18

```sh {"id":"01HT12PETTP6TZ21GCAHYX5JYZ"}
if idade < 18:
print("Você é menor de idade.")
elif idade == 18:
print("Você acabou de completar 18 anos.")
else:
print("Você é maior de idade.")
Saída do Exemplo
Se a variável "idade" for definida como 16, a saída será:
```


Você é menor de idade.
Se a variável "idade" for definida como 18, a saída será:

Você acabou de completar 18 anos.
Se a variável "idade" for definida como 20, a saída será:

Você é maior de idade.
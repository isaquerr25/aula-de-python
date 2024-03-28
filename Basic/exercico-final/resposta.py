import re

def validar_cpf(cpf):
    # Remove todos os caracteres que não sejam dígitos
    cpf = re.sub(r'\D', '', cpf)
    
    # Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False
    
    # Verifica se todos os dígitos do CPF são iguais
    if len(set(cpf)) == 1:
        return False
    
    # Calcula o primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    resto = (soma * 10) % 11
    if resto == 10:
        resto = 0
    if resto != int(cpf[9]):
        return False
    
    # Calcula o segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    resto = (soma * 10) % 11
    if resto == 10:
        resto = 0
    if resto != int(cpf[10]):
        return False
    
    return True

# Testar a função de validação de CPF
cpf = "052.420.401-22"
if validar_cpf(cpf):
    print("O CPF", cpf, "é válido.")
else:
    print("O CPF", cpf, "não é válido.")

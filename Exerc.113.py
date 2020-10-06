# Exercicio 113

# 113: Reescreva a função leiaInt() que fizemos no desafio 104, 
# incluindo agora a possibilidade da digitação de um número de tipo inválido. 
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

def leiaInt(num):
    while True:
        try:
            numero = int(input(num))
        except(ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número inteiro válido!\033[m')
            continue
        except(KeyboardInterrupt):
            print('\033[0;31mERRO! Programa interrompido pelo usuario!\033[m')
            return 0
        else:
            return numero

def leiaFloat(num):
    while True:
        try:
            numero = float(input(num))
        except(ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número real válido!\033[m')
            continue
        except(KeyboardInterrupt):
            print('\033[0;31mERRO! Programa interrompido pelo usuario!\033[m')
            return 0
        else:
            return numero

     
numeroInt = leiaInt('Digite um número inteiro: ')
numeroFloat = leiaFloat('Digite um número real: ')

print(f'O número inteiro digitado foi {numeroInt} e o número real {numeroFloat}.')
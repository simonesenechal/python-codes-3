# Exercicio 104

# 104: Crie um programa que tenha a função leiaInt(), 
# que vai funcionar de forma semelhante ‘a função input() do Python, 
# só que fazendo a validação para aceitar apenas um valor numérico. 
# Ex: n = leiaInt(‘Digite um n: ‘)

def leiaInt(num):
    ok = False
    valor = 0
    while True:
        numero = str(input(num))
        if numero.isnumeric():
            valor = int(numero)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido!\033[m')
        if ok:
            break
    return valor 
            



numero = leiaInt('Digite um número inteiro: ')
print(f'O número digitado foi {numero}.')
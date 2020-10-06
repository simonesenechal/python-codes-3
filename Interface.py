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


def linha(tam=42):
    return '-' * tam

def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opção = leiaInt('\033[32mSua opção: \033[m')
    return opção
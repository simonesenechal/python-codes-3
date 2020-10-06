def metade(preço, formatação=False):
    resultado = preço / 2
    return resultado if formatação is False else moeda(resultado)


def aumentar(preço, taxa=0, formatação=False):
    resultado = preço + (preço * taxa/100)
    return resultado if formatação is False else moeda(resultado)


def dobro(preço, formatação=False):
    resultado = preço * 2
    return resultado if formatação is False else moeda(resultado)


def diminuir(preço, taxa=0, formatação=False):
    resultado = preço - (preço * taxa/100)
    return resultado if formatação is False else moeda(resultado)


def moeda(preço, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')


def resumo(preço=0, taxaa=10, taxar=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'{taxaa}% aumento: \t\t{aumentar(preço, taxaa, True)}')
    print(f'{taxar}% redução: \t\t{diminuir(preço, taxar, True)}')
    print('-' * 30)

def leiadinheiro(msg):
    valido = False
    while not valido:
        entrada = input(msg).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO: \"{entrada}\"é um valor inválido!\033[m')
        else:
            valido = True
            return float(entrada)

            
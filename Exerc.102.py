# Exercicio 102

# 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: 
# o primeiro que indique o número a calcular 
# e outro chamado show, que será um valor lógico (opcional) 
# indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

from math import factorial


def fatorial(numero, show=False):
    """[Calcula o fatorial de um numero.
    Para numero: um número a ser calculado
    Para show: (opcional) mostrar ou não a conta
    return: O valor do Fatorial de um número n.]
    """

    f = 1
    for i in range(numero, 0, -1):
        if show:
            print(i, end = '')
            if i > 1: 
                print(' x ', end = '')
            else:
                print(' = ', end = '')
        f *= i
    return f 
        
opção = int(input('fatorial: '))
resultado = fatorial(opção, False)

print(f'O fatorial de {opção} é: {resultado}')


help(fatorial)



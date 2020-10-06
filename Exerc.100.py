# Exercicio 100

# 100: Faça um programa que tenha uma lista chamada números 
# e duas funções chamadas sorteia() e somaPar(). 
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista 
# e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint

numeros = []


def sorteia_numero(a, b):
    num = randint(a, b)
    return num

def verifica_num_duplicado(num):
    if num in numeros:
        return True
    else:
        return False

def adiciona_lista(num):
    numeros.append(num)

def ordenar_lista(lista):
    return sorted(lista)

def soma_pares(lista):
    pares = 0

    for num in lista:
        if num % 2 == 0:
            pares += num

    return pares   
    
def exibe_lista(lista):
    print(f'Os números sorteados foram: {lista}')
    
while len(numeros) != 5:
    num_sorteado = sorteia_numero(0, 50)

    if verifica_num_duplicado(num_sorteado):
        adiciona_lista_repetida(num_sorteado)
    else:
        adiciona_lista(num_sorteado)

ordenados = ordenar_lista(numeros)
exibe_lista(ordenados)

soma_pares = soma_pares(numeros)
print(f'A soma dos números pares da lista é: {soma_pares}')



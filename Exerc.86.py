# Exercicio 86

# 086: Crie um programa que declare uma matriz de dimensão 3×3 
# e preencha com valores lidos pelo teclado. 
# No final, mostre a matriz na tela, com a formatação correta.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for n in range(0,3):
    for l in range(0,3):
        matriz[n][l] = int(input(f'Digite um valor para a posição {n}, {l}: '))

for n in range(0, 3):
    for l in range(0, 3):
        print(f'{[matriz[n][l]]}', end = ' ')
    print( )






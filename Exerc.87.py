# Exercicio 87

# 087: Aprimore o desafio anterior, mostrando no final:     
                                               
# A) A soma de todos os valores pares digitados.       
# B) A soma dos valores da terceira coluna.                                                                                                      
# C) O maior valor da segunda linha.

matriz = [[0, 0 , 0], [0, 0, 0], [0, 0, 0]]
soma_pares = 0
soma_colunas = 0
maior = matriz[1][0]

for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input(f'Digite um valor para a posição {i}, {j}: '))

        if matriz[i][j] % 2 == 0:
            soma_pares += matriz[i][j]

        if j == 2:
            soma_colunas += matriz[i][j]

for i in range(3):
    for j in range(3):
        print(f'{[matriz[i][j]]}', end = ' ')
    print( )


if matriz[1][1] > maior:
    maior = matriz[1][1]
if matriz[1][2] > maior:
    maior = matriz[1][2]

print(f'A soma de todos os valores pares: {soma_pares}')
print(f'A soma da terceira coluna é igual {soma_colunas}')
print(f'O maior valor da segunda linha é {maior}')





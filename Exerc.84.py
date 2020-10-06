# Exercicio 84

#084: Faça um programa que leia nome e peso de várias pessoas,                                      
# guardando tudo em uma lista. No final, mostre:                                                              
# A) Quantas pessoas foram cadastradas.                                                                                                              
# B) Uma listagem com as pessoas mais pesadas.                                                                                                    
# C) Uma listagem com as pessoas mais leves.

dados = []
pessoas = []
maior = menor = 0

while True:
    dados.append(input('Nome: '))
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] < menor:
            menor = dados[1]
        if dados[1] > maior:
            maior = dados[1]
            
    pessoas.append(dados[:])
    dados.clear()
    
    question = ' '
    while question not in 'SN':
        question = input('Deseja continuar [S/N]? ').strip().upper()
    if question == 'N':
        break

print('--' * 30)
print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'O maior peso foi {maior}kg, Peso de',  end = ' ')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}]', end=' ')
print(' ')
print(f'O menor peso foi {menor}kg, Peso de', end = ' ')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}]', end = ' ')
print(' ')





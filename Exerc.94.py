# Exercicio 94

# 094: Crie um programa que leia nome, sexo e idade de várias pessoas, 
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. 
# No final, mostre: 
# A) Quantas pessoas foram cadastradas 
# B) A média de idade 
# C) Uma lista com as mulheres 
# D) Uma lista de pessoas com idade acima da média

pessoas = []
cadastro = {}
mulheres = []
idade_total = 0

while True:
    cadastro['nome'] = input('Nome: ').capitalize()
    sexo = input('Sexo: ').strip().upper()

    while sexo not in 'FM':
        print('Erro, digite uma opção válida [F/M]')
        sexo = input('Sexo: ').strip().upper()

    cadastro['sexo'] = sexo
    cadastro['idade'] = int(input('Idade: '))
    idade_total += cadastro['idade']

    pessoas.append(cadastro.copy())
    
    if sexo in 'Ff':
        mulheres.append(cadastro['nome'])

    media_idade = idade_total / len(pessoas)

    continuação = ' '
    while continuação not in 'NS':
        continuação = input('Deseja continuar [S/N]: ').strip().upper()
    
    if continuação == 'N':
        break

print(f'\nAo todo temos {len(pessoas)} pessoas cadastradas.')
print(f'A média de idade é de {media_idade:.2f} anos.')
print(f'As mulheres cadastradas foram: ')
for m in mulheres:
    print(f'\t - {m}')
print(f'\nAs pessoas com idade acima da média são:')
for p in pessoas:
    if p['idade'] >= media_idade:
        for k, v in p.items():
            print(f'{k} = {v}, ', end = ' ')
        print( )




# Exercicio 90

# 090: Faça um programa que leia nome e média de um aluno, 
# guardando também a situação em um dicionário. 
# No final, mostre o conteúdo da estrutura na tela.

dados = {}

dados['nome'] = input('Nome do aluno: ')
dados['media'] = float(input('Média do aluno: '))
limite = 7
situação = ' '

if dados['media'] >= limite:
    dados['situação'] = 'APROVADO'
elif 5 <= dados['media'] < 7:
    dados['situação']  = 'RECUPERAÇÃO'
else: 
    dados['situação']  = 'REPROVADO'

for k, v in dados.items():
    print(f'  - {k} é igual a {v}')
    
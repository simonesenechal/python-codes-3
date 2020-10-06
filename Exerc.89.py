# Exercicio 89

# 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. 
# No final, mostre um boletim contendo a média de cada um e permita 
# que o usuário possa mostrar as notas de cada aluno individualmente.

lista = []

while True:
    nome = input('Nome do aluno: ')
    nota1 = float(input('Primeira nota: '))
    nota2 = float(input('Segunda nota: '))
    media = (nota1 + nota2) / 2

    lista.append([nome, [(nota1, nota2)], media])

    question = ' '
    while question not in 'SN':
        question = input('Deseja continuar [S/N]? ').strip().upper()
    if question == 'N':
        break

print('--' * 30)
print(f'{"Nº.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('--' * 30)

for i, j in enumerate(lista):
    print(f'{i:<4} {j[0]:<10}{j[2]:>8.1f}')

while True:
    print('--' * 30)
    opção = int(input('De qual aluno deseja ver as notas? (999 interrompe): '))
    if opção == 999:
        print(f'FINALIZANDO...')
        break
    if opção <= len(lista) - 1:
        print(f'Notas de {lista[opção][0]} são {lista[opção][1]}')

print(f'--- VOLTE SEMPRE! --- ')




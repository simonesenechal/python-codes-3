# Exercicio 92

# 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho 
# e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, 
# o dicionário receberá também o ano de contratação e o salário. 
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime

pessoas = {}

pessoas['nome'] = input('Nome da pessoa: ')
nascimento = int(input('Ano de nascimento: '))
pessoas['idade'] = datetime.now().year - nascimento
pessoas['CTPS'] = int(input('Número CTPS (0 não tem): '))

if pessoas['CTPS'] != 0:
    pessoas['ano_contrato'] = int(input('Ano da contratação: '))
    pessoas['salario'] = float(input('Valor do salário: R$'))
    pessoas['aposentadoria'] = pessoas['idade'] + ((pessoas['ano_contrato'] + 35) -datetime.now().year)

print('--' * 30)

for i, j in pessoas.items():
    print(f'    - {i} tem o valor {j}')

    
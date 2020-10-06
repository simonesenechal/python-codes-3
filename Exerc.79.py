# Exercicio 79

# 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
# Caso o número já exista lá dentro, ele não será adicionado. 
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

lista = []

while True:
    num = int(input('Digite um valor: '))
    
    if num not in lista:
        lista.append(num)
        print(f'Valor adicionado com sucesso...')
    else:
        print(f'Este valor já existe!')
     
    escolha = ' '
    while escolha not in 'NS':
        escolha = input('Deseja continuar? [S/N] ').upper().strip()
    if escolha == 'N':
        break

print(f'Você digitou os valores: {sorted(lista)}')




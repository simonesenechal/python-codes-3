# Exercicio 82

# 082: Crie um programa que vai ler vários números e colocar em uma lista. 
# Depois disso, crie duas listas extras que vão conter apenas os valores pares 
# e os valores ímpares digitados, respectivamente. 
# Ao final, mostre o conteúdo das três listas geradas.

lista = []

while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    escolha = ' '
    while escolha not in 'SN':
        escolha = input('Deseja continuar [S/N]: ').strip().upper()
    if escolha == 'N':
        break

print(f'A lista completa é:  {lista}')

par = []
impar = []

for numero in lista:
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)

print(f'Valores ímpares {impar}')
print(f'Lista de números pares: {par}')




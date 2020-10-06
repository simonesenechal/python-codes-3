# Exercicio 81

# 081: Crie um programa que vai ler vários números e colocar em uma lista.                  
# Depois disso, mostre:                                                                                                     
# A) Quantos números foram digitados.                                                               
# B) A lista de valores, ordenada de forma decrescente.                                                                                          
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = []

while True:
    num = int(input('Digite um valor: '))
    lista.append(num)

    escolha = ' '
    while escolha not in 'SN':
        escolha = input('Deseja continuar [S/N]: ').strip().upper()
    if escolha == 'N':
        break

print(f'Foram digitados {len(lista)} números na lista.')
lista.sort(reverse = True)
print(f'A ordem decrescente dos números são {lista}')

if 5 in lista:
    print(f'O valor 5 faz parte da lista.')
else:
    print(f'O valor 5 não faz parte da lista.')
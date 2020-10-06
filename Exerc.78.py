# Exercicio 78

# 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

valores = []
maior = []
menor = []

for cont in range(0, 5):
    valores.append(int(input('Digite um número: ')))
for c, v in enumerate(valores):
    if v == max(valores):
        maior.append(c)
    if v == min(valores):
        menor.append(c)
print(f'Os valores digitados foram: {valores}')
print(f'O maior valor encontrado foi: {max(valores)} na posição {maior}')
print(f'O menor valor encontrado foi: {min(valores)} na posição {menor}')







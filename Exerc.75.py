# Exercicio 75

# Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. 
# No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

num = (int(input('Digite o primeiro número: ')), 
       int(input('Digite o segundo número: ')), 
       int(input('Digite o terceiro número: ')), 
       int(input('Digite o quarto número: ')))

print(f'Os números digitados foram {num}')
print(f'O número 9 apareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'O número 3 apareceu na posição {num.index(3)+1}')
else:
    print(f'O número 3 não foi digitado.')
print(f'Os valores pares digitados foram:', end = ' ')
for n in num:
    if n % 2 == 0:
        print(n, end = ' ')
        



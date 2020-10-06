# Exercicio 107

# 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas 
# aumentar(), diminuir(), dobro() e metade(). 
# Faça também um programa que importe esse módulo e use algumas dessas funções.

import Moeda

valor = float(input('Digite um preço: R$'))

print(f'O dobro de R${valor} é R${Moeda.dobro(valor)}')
print(f'A metade de R${valor} é {Moeda.metade(valor)}')
print(f'O aumento de 10% de R${valor} é {Moeda.aumentar(valor)}')
print(f'A dimunuição em 10% de R${valor} é {Moeda.diminuir(valor)}')





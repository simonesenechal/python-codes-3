# Exercicio 108

#108: Adapte o código do desafio #107, 
# criando uma função adicional chamada moeda() que consiga 
# mostrar os números como um valor monetário formatado.

import Moeda

valor = float(input('Digite um preço: R$'))

print(f'O dobro de {Moeda.moeda(valor)} é {Moeda.moeda(Moeda.dobro(valor))}')
print(f'A metade de {Moeda.moeda(valor)} é {Moeda.moeda(Moeda.metade(valor))}')
print(f'O aumento de 10% de {Moeda.moeda(valor)} é {Moeda.moeda(Moeda.aumentar(valor))}')
print(f'A dimunuição em 10% de {Moeda.moeda(valor)} é {Moeda.moeda(Moeda.diminuir(valor))}')

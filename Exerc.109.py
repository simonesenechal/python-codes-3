# Exercicio 109

#109: Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, 
# informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), 
# desenvolvida no desafio 108.

import Moeda

valor = float(input('Digite um preço: R$'))

print(f'O dobro de {Moeda.moeda(valor)} é {Moeda.dobro(valor, True)}')
print(f'A metade de {Moeda.moeda(valor)} é {Moeda.metade(valor, True)}')
print(f'O aumento de 10% de {Moeda.moeda(valor)} é {Moeda.aumentar(valor, True)}')
print(f'A dimunuição em 10% de {Moeda.moeda(valor)} é {Moeda.diminuir(valor, True)}')

# Exercicio 91

#  091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. 
# Guarde esses resultados em um dicionário em Python. 
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
import operator


jogo = {}
dado = [1, 6]

print(f'Valores sorteados: ')

for i in range(4):
    num = randint(dado[0], dado[1])
    player = 'jogador' + str(i+1)
    jogo[player] = num


for k, v in jogo.items():
    print(f'O {k} sorteou {v} no dado.')

print(' ')
print(f'--' * 20)
print(f'{"RANKING DOS JOGADORES":^40}')
print(f'--' * 20)
sleep(1)

sortedDict = sorted(jogo.items(), key=operator.itemgetter(1), reverse=True)

for i, v in enumerate(sortedDict):
    print(f'  {i+1}º lugar: {v[0]} com {v[1]}')

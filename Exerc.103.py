# Exercicio 103

#  103: Faça um programa que tenha uma função chamada ficha(), 
# que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. 
# O programa deverá ser capaz de mostrar a ficha do jogador, 
# mesmo que algum dado não tenha sido informado corretamente.

def ficha(jogador ='<desconhecido>', gols = 0):

    print(f'O jogador {jogador} fez {gols} gols no jogo.')

nome = input('Nome do jogador: ')
quantidade_gols = input('Número de gols: ')

if quantidade_gols.isnumeric():
    quantidade_gols = int(quantidade_gols)
else:
    quantidade_gols = 0

if nome.strip() == '':
    ficha(gols = quantidade_gols)
else:
    ficha(nome, quantidade_gols)


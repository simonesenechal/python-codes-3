# Exercicio 93

# 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
# O programa vai ler o nome do jogador e quantas partidas ele jogou. 
# Depois vai ler a quantidade de gols feitos em cada partida. 
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

nome = input('Nome do Jogador: ')
jogos = int(input('Quantas partidas jogadas? '))

aproveitamento = {'Jogador': nome,
                  'Gols': [],
                  'Total_gols': 0}

for i in range(jogos):
    num_gols = int(input(f'Quantos gols na partida {i+1}: '))
    partida = i+1

    aproveitamento['Gols'].append(num_gols)
    aproveitamento['Total_gols'] += num_gols
    
print('--' * 30)
print(aproveitamento)
print('--' * 30)

for k, v in aproveitamento.items():
    print(f'O campo {k} tem o valor {v}')

print('-=' * 30)
print(f'O jogador {nome} jogou {jogos} partidas.')

for i, v in enumerate(aproveitamento['Gols']):
    print(f'\t=> Na Partida {i+1}, fez {v} gols. ')

print(f"Foi um total de {aproveitamento['Total_gols']} gols.")

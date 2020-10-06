# Exercico 73

# 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, 
# na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.


times = ('Palmeiras', 'Fluminense', 'Atletico Mineiro', 'Santos', 'Bahia', 
'Botafogo', 'Internacional', 'Sao Paulo', 'Juventude', 'Chapecoense', 'Corinthians',
'Cruzeiro', 'America', 'Vasco', 'Parana', 'Fortaleza', 'Gremio', 'Sport', 'Ceara', 'Goias')

print('--' * 20)
print(f'Tabela do Brasileirão')
print('--' * 20)

for t in times:
    print(t)

print(f'Os cinco primeiros colocados na tabela são: {times[:5]}')
print(f'Os quatro últimos colocados na tabela são: {times[-4:]}')
print(f'Os times em ordem alfabética fica: {sorted(times)}')
print(f'O {times[9]} está na {len(times[1:11])}ª posição na tabela.')
print(f'O Chapecoense está na {times.index("Chapecoense")+1}ª posição na tabela.')



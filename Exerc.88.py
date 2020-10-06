# Exercicio 88

# 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites. 
# O programa vai perguntar quantos jogos serão gerados 
# e vai sortear 6 números entre 1 e 60 para cada jogo, 
# cadastrando tudo em uma lista composta.


from random import randint


intervalo_jogos = [1, 60]
jogos_mega = []

qtd_jogos = int(input('Qual a quantidade de jogos? '))

for i in range(qtd_jogos):
    jogo_temp = []

    for j in range(6):
        num = randint(intervalo_jogos[0], intervalo_jogos[1])

        while num in jogo_temp:
            num = randint(intervalo_jogos[0], intervalo_jogos[1])
        
        jogo_temp.append(num)

    jogos_mega.append(jogo_temp)


for i, v in enumerate(jogos_mega):
    v.sort()
    print(f'Jogo {(i)+1}: {v}')








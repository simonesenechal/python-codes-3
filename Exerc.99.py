# Exercicio 99

# 099: Faça um programa que tenha uma função chamada maior(), 
# que receba vários parâmetros com valores inteiros. 
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.


from time import sleep

def maior(*args):
    contador = maior = 0
    print('-' * 40 )
    print('Analisando os valores passados...')
    print(' ')

    for valor in args:
        print(f'{valor}', end = ' ', flush=True)
        sleep(0.3)

        if contador == 0:
            maior = valor
        else: 
            if valor > maior:
                maior = valor 
        contador += 1
        
    print(f'Foram informados {contador} valores ao todo.')
    print(f'O maior valor informado foi {maior}')
        

maior(9, 34, 3, 2)
maior(10, 78)
maior(7, 56, 90, 4, 3, 0)
maior()
maior(4)



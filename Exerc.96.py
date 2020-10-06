# Exercicio 96

# 096: Faça um programa que tenha uma função chamada área(), 
# que receba as dimensões de um terreno retangular (largura e comprimento) 
# e mostre a área do terreno.

def area(larg, compr):
    area_total = larg * compr
    print(f'A área total do terreno no tamanho {larg} x {compr} é de {area_total:.2f}m².')


print('Controle de Terrenos')
print('--' * 20)

largura = float(input('Largura(m):  '))
comprimento = float(input('Comprimento(m): '))

area(largura, comprimento)









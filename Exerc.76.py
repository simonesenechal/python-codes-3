# Exercicio 76

# 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. 
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

produtos = ('agulha', 2.99, 
            'linha meada', 1.99, 
            'tesoura', 24.99, 
            'bastidor', 16.99, 
            'caneta', 20.99,
            'algodão cru', 9.99,
            'cola', 1.99,
            'linha de costura', 0.50)
print('-' * 40)
print(f'{"TABELA DE PREÇOS":^40}')
print('-' * 40)

for itens in range(0, len(produtos)):
    if itens % 2 == 0:
        print(f'{produtos[itens]:.<30}', end = ' ')
    else:
        print(f'R${produtos[itens]:>6.2f}')
print('-' * 40)
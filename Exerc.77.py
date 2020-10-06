# Exercicio 77

# 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). 
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('amor', 'gratidao', 'paz', 'alegria', 'felicidade', 'compreensao',
            'amizade', 'saude', 'transformacao', 'emocao')

for letra in palavras:
    print(f'\nNa palavra {letra.upper()} temos ', end = '')
    for vogal in letra:
        if vogal.lower() in 'aeiou':
            print(vogal, end = '')


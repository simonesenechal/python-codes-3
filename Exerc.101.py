# Exercicio 101

# 101: Crie um programa que tenha uma função chamada voto() que vai receber 
# como parâmetro o ano de nascimento de uma pessoa, 
# retornando um valor literal indicando se uma pessoa 
# tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

from datetime import date


def voto(nascimento: int) -> str:
    ano_atual = date.today().year 
    idade_atual = ano_atual - nascimento

    if 16 <= idade_atual < 18 or idade_atual > 70:
        return f'Com {idade_atual} anos: VOTO OPCIONAL! '
    elif idade_atual < 16:
        return f'Com {idade_atual} anos: VOTO NÃO VOTA! '
    else:
        return f'Com {idade_atual} anos: VOTO OBRIGATÓRIO!'
        

ano_nascimento = int(input('Ano de nascimento: '))
resultado = voto(ano_nascimento)

print(resultado)
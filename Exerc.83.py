# Exercicio 83

# 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos 
# e fechados na ordem correta.


expressao = input('Digite uma expressão usando parênteses: ')

lista = []

for elemento in expressao:
    if elemento == '(':
        lista.append('(')
    elif elemento == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('A expressão está válida!')
else:
    print('A expressão está inválida!')

    



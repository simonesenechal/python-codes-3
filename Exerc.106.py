# Exercicio 106

#  106: Faça um mini-sistema que utilize o Interactive Help do Python. 
# O usuário vai digitar o comando e o manual vai aparecer. 
# Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. 
# Importante: use cores.

from time import sleep

cores = ('\033[m',
         '\033[0;30;41m',
         '\033[0;30;42m',
         '\033[0;30;43m',
         '\033[0;30;44m',
         '\033[0;30;45m',
         '\033[7;30m',
        );

def ajuda(comando):
    titulo(f'Acessando o manual do comando! \'{comando}\'', 4)
    print(cores[6], end = '')
    help(comando)
    print(cores[0], end = '')
    sleep(2)

def titulo(msg, cor=0):
    tamanho = len(msg) + 4
    print(cores[cor], end = '')
    print('-' * tamanho)
    print(f'  {msg}')
    print('-' * tamanho)
    print(cores[0], end = '')
    sleep(1)

comando_principal = ''
while True:
    titulo('SISTEMA DE AJUDA PYHELP', 2)
    comando_principal = input("Função ou Biblioteca > ")
    if comando_principal.upper() == 'FIM':
        break
    else:
        ajuda(comando_principal)
titulo('ATÉ LOGO...', 1)


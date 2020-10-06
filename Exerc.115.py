import Interface
import Arquivo

from time import sleep

nome_arquivo = 'exerciciofinal115.txt'

if not Arquivo.arquivoExiste(nome_arquivo):
    Arquivo.criarArquivo(nome_arquivo)
    
while True:
    resposta = Interface.menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta == 1:
        # Opção de listar um conteúdo do arqu1ivo 
        Arquivo.lerArquivo(nome_arquivo)
    elif resposta == 2:
        # Cadastrar uma nova pessoa
        Interface.cabeçalho('NOVO CADASTRO')
        nome = input('Nome completo: ')
        idade = Interface.leiaInt('Idade: ')
        Arquivo.cadastrar(nome_arquivo, nome, idade)
    elif resposta == 3:
        # Opção par sair do sistema
        print('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')


import Interface

def arquivoExiste(nome):
    try: 
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Errro ao ler o arquivo!')
    else: 
        Interface.cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dados = linha.split(':')
            dados[1] = dados[1].replace('\n', '')
            print(f'{dados[0]:<30}{dados[1]:>3} anos')
    finally:
        a.close()


def cadastrar(nome_arquivo, nome='desconhecido', idade=0):
    try:
        a = open(arquivo, 'at')
    except:
        print(f'Houve um erro na abertura do arquivo!')
    else: 
        try:
            a.write(f'{nome}; {idade}\n')
        except:
            print('Houve um erro na escrita dos dados')
        else:
            print(f'Novo registro de {nome} adicionado!')
            a.close()
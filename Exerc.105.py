# Exercicio 105

# 105: Faça um programa que tenha uma função notas() que pode receber 
# várias notas de alunos e vai retornar um dicionário com as seguintes informações:

# - Quantidade de notas
# - A maior nota  
# - A média da turma 
# - A situação (opcional) 
# Adicione também as docstrings dessa função para consulta pelo desenvolvedor.


def notas(*numeros, situação=False):
    """ 
    - Função para analisar notas e situações de vários alunos.
    para número: uma ou mais notas de alunos
    para situação: valor opcional, indicando se deve ou não mostrar a nota do aluno 
    return: dicionário com várias informações sobre a situação da turma.
    """
    dados = {}
    dados['total'] = len(numeros)
    dados['maior'] = max(numeros)
    dados['menor'] = min(numeros)
    dados['media'] = sum(numeros) / len(numeros)

    if situação:
        if dados['media'] >= 7: 
            dados['situação'] = 'BOA'
        elif dados['media'] >= 5:
            dados['situação'] = 'RAZOAVEL'
        else:
            dados['situação'] = 'RUIM'
            
    return dados

aluno = notas(9, 9, 10, 8.9, 5.2, situação=True)
print(aluno)
help(notas)
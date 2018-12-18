import requests
import json


def requisicao(titulo):
    try:
        req = requests.get(
            'http://www.omdbapi.com/?i=tt3896198&apikey=ddbec73e&t=' + titulo)
        dicionario = json.loads(req.text)
        return dicionario
    except:
        print('Erro na conexão')
        return None


sair = False

while not sair:
    opcao = input('Escreva o nome do filme ou SAIR para fechar: ')

    if opcao == 'SAIR':
        sair = True
    else:
        pesquisa = requisicao(opcao)

        if pesquisa['Response'] == 'False':
            print('Filme não encontrado')
        else:
            # detalhes do filme
            print(pesquisa['Title'], '\n')
            print(pesquisa['Poster'], '\n')
            print('demais detalhes\n', pesquisa)

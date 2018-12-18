import requests  # Beautiful Soup 4 BS4

# requisicao = None

cabecalho = {'User-agent': 'Windows 12', 'Referer': 'https://google.com'}

meus_cookies = {'Ultima-visita': '10-10-2012'}

dados = {'username': 'roi', 'password': '123'}
try:
    requisicao = requests.get(
        'https://putsreq.com/Ib4E0MaFP2kc5kxC7K2t', headers=cabecalho, cookies=meus_cookies, data=dados)
    print(requisicao.text)
except Exception as err:
    print('problemas', err)

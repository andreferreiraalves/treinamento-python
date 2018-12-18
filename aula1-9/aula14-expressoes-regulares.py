import re

string_de_teste = 'ronaldo@gmail.com tet@email.sp'

# encontra o primeiro
# padrao = re.search(r'gat\w', string_de_teste)  # Raw String
padrao = re.findall(r'[\w\.-]+@[\w-]+\.[\w-\.-]+', string_de_teste)  # Raw String

if padrao:
    # print(padrao.group())
    print(padrao)
else:
    print('padrão não encontrado')

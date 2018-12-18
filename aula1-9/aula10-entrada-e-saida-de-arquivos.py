'''
# abre no modo de leitura
open('arquivo.txt', 'r')

# abre no modo escrita
open('arquivo.txt', 'w')

# leitura e escrita
open('arquivo.txt', 'r+')

# escrita no modo append, adiciona no final do arquivo
open('arquivo.txt', 'a')

# demais arquivos que não forem no modo texto
open('arquivo.txt', 'b')

# abre o arquivo binário em modo leitura
open('arquivo.txt', 'rb')
'''

arquivo = open('arquivo.txt', 'w')

arquivo.write('oi eu sou o goku')
arquivo.write('oi eu sou o goku 2')

arquivo.close()

arquivo = open('arquivo.txt')
print(arquivo.read())

for linha in arquivo:
    print(linha)

arquivo.close()

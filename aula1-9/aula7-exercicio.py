'''
Exercicio: escreva uma função que recebe um objeto de coleção
e retorna o valor do maior numero dentro dessa coleção
faça outra função que retorna o menor numero dessa coleção
'''


def maior_numero(lista):
    lista.sort()
    return lista[len(lista) - 1]


def menor_numero(lista):
    lista.sort()
    return lista[0]


lista = [10, 9, 1]
print('maior numero', maior_numero(lista))
print('menor número', menor_numero(lista))

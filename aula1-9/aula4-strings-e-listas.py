'''
frase = 'oi, eu sou o goku'

print(frase[0], frase[4])
'''

frase = 'Oi, eu sou o Goku'

lista = ['andre', 'ronaldo', 'roi']

print(frase[3:10])

# ultimo número são "pulos"
print(frase[0:10:2])
print(lista[-1])
print(frase[::-1])

lista.append('roi2')
lista.append('roi3')

print(lista)

lista.remove('roi3')
print(lista)

# lista.clear()
lista.insert(1, 'creosvaldo')
print(lista)

lista[0] = lista[0] + ' alterador'

print(lista)

contador_joao = lista.count('joão')
print(contador_joao, len(lista))

print(frase.lower())
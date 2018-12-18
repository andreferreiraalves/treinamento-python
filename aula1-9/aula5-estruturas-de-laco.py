nomes = ['guilherme', 'marcelo', 'joão', 'julia']
# lista_de_numeros = range(5)
lista_de_numeros = range(5, 10, 2)

for item in lista_de_numeros:
	print(item)

print('\n')

for i in range(4):
	print(nomes[i])

print('\n')

for i in range(len(nomes)):
	print(nomes[i])

print('\n')	

i = 0

while i < 10:
	print('número', i)
	i += 1
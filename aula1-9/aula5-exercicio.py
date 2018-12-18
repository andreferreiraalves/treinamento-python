'''
Faça um programa que leia a quantidade de pessoas que serão convidadas para uma festa
Após isso o programa irá perguntar o nome de todas as pessoas e colocar numa lista de convidados
após isso irá imprimir todos os nomes da lista
'''



lista_pessoas = []

while True:
	opcao = input('1 -> adiciona pessoas\n2 -> Lista as pessoas\n3 -> Sair\n')

	if opcao == '1':
		lista_pessoas.append(input('\nDigite o nome do hóspede: '))
	elif opcao == '2':
		for nome in lista_pessoas:
			print(nome)
	elif opcao == '3':
		break
	else:
		print('opcao não encontrada')


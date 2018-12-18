'''
Faça um programa que pergunte a idade, o peso e a altura
de uma pessoa e decide se ela está apta a ser do exército

peso maior ou igual a 60 kg
e medir mais ou igual a 1,7 metros
'''

print('entrar exército')

peso = input('Digite o peso: ')
altura = input('Digite a altura: ')

if (int(peso) >= 60) and (float(altura) >= 1.7) :
	print('pronto para o exército :)')
else:
	print('vc não está pronto')
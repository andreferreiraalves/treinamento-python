from veiculo import Veiculo
from carro import Carro

caminhao_rosa = Veiculo('rosa', '4', 'marca1', 10)

print(caminhao_rosa.tanque)

print('abastecendo:', caminhao_rosa.abastecer(50))

print(caminhao_rosa.tanque)

carro_ford = Carro('azul', 'ford', 50)

carro_ford.abastecer(10)
carro_ford.abastecer(10)

print(carro_ford)


from veiculo import Veiculo

# herança


class Carro(Veiculo):
    def __init__(self, cor, marca, tanque):
        Veiculo.__init__(self, cor, '4', marca, tanque)

    def abastecer(self, litros):
        if self.tanque + litros > 50:
            print('erro: tanque cheio')
        else:
            self.tanque += litros

class pessoa():
    def __init__(self, nome):
        self.nome = nome


    def andar (self, velocidade):
        print(self.nome, 'voce esta  se deslocando a:', velocidade,'km/h')

p = pessoa('wagner')
p2 = pessoa('joão')

print(p)

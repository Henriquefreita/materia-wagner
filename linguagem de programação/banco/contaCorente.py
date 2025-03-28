from conta import Conta
class contaCorrente(Conta):
    def __init__(self, agencia, cliente, saldo = 0, limite=1000):
        super().__init__(agencia, cliente, saldo)
        self.__limite = limite

    def saque(self):
        while True:
            sacar = float(input('qual o valor que voce deseja transacionar \n(o valor devera ser menor que 2000: '))
            if (sacar <=self.saldo + self.__limite) and (sacar <= 2000) and (sacar %10 == 0):
                self.saldo = self.saldo - sacar
                print('valor retirado com sucesso')
                print(f' seu saldo é {self.saldo:.2f}')
                return contaCorrente.valor
            else:
                print('valor invalido')

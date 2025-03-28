from conta import Conta
class contaPoupança(Conta):
    def __init__(self, agencia, cliente, saldo = 0, ):
        super().__init__(agencia, cliente, saldo)

    def saque(self):
        while True:
            sacar = float(input('qual o valor que voce deseja transacionar \n(o valor devera ser menor que 2000  : '))
            if (sacar <=self.saldo) and (sacar <= 2000) and (sacar %10 == 0):
                self.saldo = self.saldo - sacar
                print('operação realida com sucesso')
                print(f' seu saldo é {self.saldo:.2f}')
                return contaPoupança.Valor
            else:
                print('valor invalido')
    def tranferencia(self,contaDestinatario):
        valor = self.sacar()
        contaDestinatario.saldo+=valor
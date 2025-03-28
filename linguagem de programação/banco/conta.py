from cliente import cliente
from agencia import agencia
from abc import ABC, abstractmethod
class Conta(ABC):
    numero_da_conta= 0
    def __init__(self, agencia:agencia, cliente:cliente, saldo:float=0.00):
        Conta.numero_da_conta += 1
        self.agencia = agencia
        self.cliente = cliente
        self.saldo = saldo
        self.numero_da_conta = f"{Conta.numero_da_conta:04}-0"

    def depositar(self):
        while True:
            deposito = float(input('so aceitamos valores multiplos de R$ 10,00\ndigite o valor a depositar: '))
            if deposito >= 10 and deposito %10 == 0:
                self.saldo = self.saldo + deposito
                print('valor depositado com sucesso')
                print(f' seu saldo é {self.saldo:.2f}')
                return
            else:
                print('valor invalido, ou valor abaixo do minimo\n tente novamente')
                
    def consultar_saldo(self):
        print("-----Saldo em Conta-----")
        print(f' seu saldo é {self.saldo:.2f}')

    @abstractmethod
    def saque(self):
        pass

    @abstractmethod
    def tranferencia(self, conta):
        pass
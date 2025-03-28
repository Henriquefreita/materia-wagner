from banco import banco
from agencia import agencia
from cliente import cliente
from conta import Conta
from contaCorente import contaCorrente
from contaPoupança import contaPoupança
from endereco import endereco
from gerente import Gerente
import os

class main():  
     bancos = []  
     agencias = []  
     clientes = []  
     contas = []  
     gerentes = []  

     def criarBancos(self):  
        b1 = banco('Banco do Brasil S.A.', 1)  
        b2 = banco('Caixa Ecônomica Federal', 104)  
        main.bancos.append(b1)  
        main.bancos.append(b2)  

     def imprimirBancos(self):  
            print("-----------Relação de Bancos-----------")  
            for banco in main.bancos:  
                print(f'Banco: {banco.nome} - id: {banco.id}'"\n", "-"*40)  

     def criarAgencias(self):  
         a1 = agencia(4742, main.bancos[0])  
         a2 = agencia(11873, main.bancos[1])  
         main.agencias.append(a1)  
         main.agencias.append(a2)  

     def imprimirAgencias(self):  
         print("-----------Relação de Agencias-----------")  
         for agencia in main.agencias:  
              print(f'Agência: {agencia.id}\nBanco: {agencia.banco.nome}\nCódigo do banco: {agencia.banco.id}'"\n","-"*40)  
      
     def criarClientes(self):  
         c1 = cliente('Arthur', '069024', '166', "023.323.727-10")  
         c2 = cliente('Wagner', '069024', '133', "133.982.342-00")  
         main.clientes.append(c1)  
         main.clientes.append(c2)  

     def imprimirClientes(self):  
         print("-----------Relação de Clientes-----------")  
         for cliente in main.clientes:  
                print(f'Cliente: {cliente.nome} Telefone:{cliente.telefone} Endereço:{cliente.endereco} Cpf:{cliente.cpf}'"\n","-"*70)  

     def CriarContas(self):  
         c1 = contaCorrente(main.agencias[0], main.clientes[0], 1320.20)  
         c2 = contaPoupança(main.agencias[1], main.clientes[1], 1320.20)  
         main.contas.append(c1)  
         main.contas.append(c2)  

     def ImprimirContas(self):  
          print("-----------Relação de Contas-----------")  
          for conta in main.contas:  
               print(f'Banco: {conta.agencia.banco.nome} N° Agência: {conta.agencia.id} N° Conta: {conta.numero_da_conta} Cliente: {conta.cliente.nome} Cpf: {conta.cliente.cpf} Saldo: {conta.saldo:.2f}'"\n","-"*120)  

     def ValidarConta(self):  
          while True:  
               self.ImprimirContas()  
               nrConta = input('Digite o número da conta que deseja acessar: ')  
               for conta in self.contas:  
                    if nrConta == conta.numero_da_conta:  
                         print('Acesso realizado com sucesso')  
                         print('Seja bem-vindo', conta.cliente.nome)  
                         return conta  
               os.system('cls')  
               print('Conta não encontrada')  

     def ValidarGerente(self):  
          if not self.gerentes:  
               self.CriarGerente()  

          nome = input("Digite seu nome: ").strip().lower()  
          usuario = input("Digite seu nome de usuário: ").strip().lower()  
          senha = input("Digite sua senha: ").strip()  

          for gerente in self.gerentes:  
               if (  
                    nome == gerente.nome.lower() and   
                    usuario == gerente.usuario.lower() and   
                    senha == gerente.senha  
               ):  
                    print(f"Dados corretos, bem-vindo {gerente.nome}!")  
                    return True  

          print("Dados incorretos, tente novamente.")  
          return False  

     def CriarGerente(self):  
          g1 = Gerente("wesley", "wesley2", "2patinhosnalagoa")  
          g2 = Gerente("Wagner", "Wagner2012", "eunaoerro")  
          main.gerentes.append(g1)  
          main.gerentes.append(g2)  

     def startCliente(self):  
          main.criarBancos()  
          main.criarAgencias()  
          main.criarClientes()  
          main.CriarContas()  
          contausuario = main.ValidarConta()  
          os.system("cls")  
          while True:  
               op = int(input("Escolha uma opção: \n(1)Consultar Saldo \n(2)Depositar  \n(3)Sacar \n(9)Sair \n"))          
               if op == 2:  
                    contausuario.deposito()  
               elif op == 1:  
                    contausuario.ConsultarSaldo()  
               elif op == 3:  
                    contausuario.Sacar()  
               elif op == 9:  
                    break                 
               else:  
                    print("Opção inválida")      

     def startGerente(self):  
          while True:  
               op = int(input("Escolha uma opção: \n(1) Imprimir Relação de Bancos\n(2) Imprimir Relação de Agências\n(3) Imprimir Relação de Clientes\n(4) Imprimir Relação de Contas \n(5)Sair \n"))          
               if op == 1:  
                    main.imprimirBancos()  
               elif op == 2:  
                    main.imprimirAgencias()  
               elif op == 3:  
                    main.imprimirClientes()  
               elif op == 4:  
                    main.ImprimirContas()  
               elif op == 5:    
                    break  
               else:  
                    print("Opção inválida")  

     def escolherTipodeUsuario(self):  
          op = int(input("Digite (1) para Gerente e (2) para Cliente: "))  
          if op == 1:  
               if main.ValidarGerente():  
                    self.startGerente()  
          elif op == 2:  
               main.startCliente()  
          else:  
               print("Incorreto, Tente novamente")  

main = main()  
main.escolherTipodeUsuario()
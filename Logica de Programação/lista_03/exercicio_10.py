saldo = 1000
while True:
    mov =    int(input('(1) Consultar saldo, (2) Efetuar saque, (3) Efetuar depósito e (4) sair.: '))
    if mov == 1:
        print(saldo)
    elif mov == 2:
        saida = float(input('quanto você deseja retirar: '))
        if saida < saldo:
            saldo = saldo - saida
            print('esse é seu saldo atualmente: ', saldo)
        print('saldo insuficiente')
    elif mov == 3:
        entrada = float(input('quanto você deseja depositar: '))
        saldo = saldo + entrada
        print('esse é seu saldo atualmente: ', saldo)
    elif mov == 4:
        break
    else:
        print('opção invalida') 
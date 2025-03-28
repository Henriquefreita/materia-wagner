from random import randint
def joguinho():
    for n in range(1,7):
        resposta = int(input("Número: "))
        if int(resposta > numero_aleatorio):
            print("É menor que",(resposta))
            print("Restam ",(7-n)," tentativas")
        elif int(resposta < numero_aleatorio):
            print("É maior que",(resposta))
            print("Restam ",(7-n)," tentativas")
        else:
            print("Você acertou!",'\n', "O número era",numero_aleatorio)
            break  
    else:
        print("Você perdeu")
        print(numero_aleatorio)
numero_aleatorio = (randint(0,100))
joguinho()

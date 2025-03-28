cont = 1
numero = int(input('digite um numero: '))
while True:
    print(cont)
    cont+=1
    if numero > 1:
        
        print(cont)
        if cont == numero:
            break
        cont+=1
        print('numero valido')
    else:
        numero = int(input('digite um numero: '))
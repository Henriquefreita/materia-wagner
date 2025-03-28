numero = int(input("Numero: "))
cont = 1
linha = 1
for i in range(numero):
    for x in range(linha):
        print(cont,end=' ')
        cont += 1
    print('')
    linha+=1
def tabuada():
    numero = int(input("Digite um número para ver a tabuada: "))
    tabuada = [numero * i for i in range(1, 11)]
    print("Tabuada do {}: {}".format(numero, tabuada))

tabuada()

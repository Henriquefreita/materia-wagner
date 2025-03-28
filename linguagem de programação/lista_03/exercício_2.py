def imprimir_maior_menor():
    numeros = []
    for i in range(10):
        numero = float(input("Digite um número do tipo float: "))
        numeros.append(numero)
    maior = max(numeros)
    menor = min(numeros)
    print("O maior número lido é:", maior)
    print("O menor número lido é:", menor)
imprimir_maior_menor()

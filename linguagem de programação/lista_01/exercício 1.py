def verificar_numero(numero):
    if numero > 0:
        return "P"
    elif  numero < 0:
        return "N"
    else:
        return "Z"
n = int(input("Digite o número: "))
print(verificar_numero(n))
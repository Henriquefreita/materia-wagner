def operação(n1,op,n2):
    if op == "*":
        return n1 * n2
    elif op == "-":
        return n1 - n2
    elif op == "/":
        return n1 / n2
    elif op == "+":
        return n1 + n2
    else:
        return "Erro"
n = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))
sinal = str(input("Digite o sinal da operação: "))
print(operação(n,sinal,n2))
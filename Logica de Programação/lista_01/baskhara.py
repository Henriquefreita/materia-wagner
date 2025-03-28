import math

def calcular_bhaskara(a, b, c):
    # Calcula o discriminante
    delta = b**2 - 4*a*c
    
    # Verifica se há raízes reais
    if delta < 0:
        return "Não existem raízes reais."
    elif delta == 0:
        x = -b / (2*a)
        return f"A única raiz é: {x}"
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return f"As raízes são: {x1} e {x2}"

# Exemplo de uso
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

print(calcular_bhaskara(a, b, c))

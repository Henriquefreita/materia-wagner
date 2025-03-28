lado_a=0
lado_b=0 
lado_c=0
def ler_dado():
    global lado_a, lado_b, lado_c
    while True:
        lado_a = int(input("Digite o primeiro lado: "))
        if lado_a > 0:
            break
    while True:
        lado_b = int(input("Digite o segundo lado: "))
        if lado_b > 0:
            break
    while True:
        lado_c = int(input("Digite o terceiro lado: "))
        if lado_c > 0:
            break

def validar_triangulo():
    if (lado_a < lado_b + lado_c) or (lado_b < lado_a + lado_c) or (lado_c < lado_a + lado_b):
        return True
    else:
        return False

def tipo_triangulo():
    if lado_a == lado_b == lado_c:
        return "Triângulo equilátero"
    elif lado_a != lado_b != lado_c:
        return "Triângulo escaleno"
    else:
        return "Triângulo isosceles"

ler_dado()
if validar_triangulo:
    print(tipo_triangulo())
else:
    print("Não é triângulo")
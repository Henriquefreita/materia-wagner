import random
def verificar_numero():
    numeros = random.sample(range(101), 20)
#    print("Lista gerada:", numeros)
    numero_usuario = int(input("Digite um número inteiro entre 0 e 100: "))
    if numero_usuario in numeros:
        print("Você ganhou!")
    else:
        print("Não foi desta vez!")
verificar_numero()

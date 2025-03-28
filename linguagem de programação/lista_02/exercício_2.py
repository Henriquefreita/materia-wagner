def divisao(a, b):
    try:
        resultado = a/ b
        return resultado

    except ValueError:
        print('erro')
    finally:
        return('fim')

print(divisao(10,2))
print(divisao(10 / '2'))

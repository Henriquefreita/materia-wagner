def contar_pares(*numeros):
    pares = 0
    for num in numeros:
        if num % 2 == 0:
            pares += 1
    return pares
print(contar_pares(1,2,3,4,5,6,7,8), "pares")
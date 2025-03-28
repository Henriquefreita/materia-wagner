def contar_positivos(*numeros):
    positivos = 0
    for num in numeros:
        if num >= 0:
            positivos += 1
    return positivos
print(contar_positivos(-3,-1,1,2,3,4,5,6,7,8), "positivos")


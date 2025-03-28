numero = int(input('digite um numero: '))
if numero % 3 == 0 and numero % 7 == 0:
    print('numero divisivel por 3 e 7')
elif numero % 3 == 0:
    print('numero divisivel por 3')
elif numero % 7 == 0:
    print('numero divisivel por 7')
else:
    print('numero não divisivel')
num = int(input('Numero: '))

if num >= 1:
    for n in range(2, num):
        if num % n == 0:
            print(num, 'Nao é primo')
            break
    else:
        print(num, 'é primo')
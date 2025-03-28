def main():
    print('vamos dividir')
    while True:
        try:
            x = input('digite o valor: ')
            x = int (x)
            y = input('digite o valor: ')
            y = int(y)
            r = x/y
            print(f'O resultado: {r}')
        except ValueError:
            print('erro de valor')
        except ZeroDivisionError:
            print('não se divide por 0 burro')
        else:
            print('acabou')
            break
main()
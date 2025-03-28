def main():
    try:
        resultados = numero + 10
        print(resultados)
    except NameError:
        print('erro')
    finally:
        print('fim')


main()


def main():

    print('inicio do main')
    funcao_01()
    print('fim do main')

def funcao_01():
    print('inicio da funcao-01')
    funcao_02()
    print('fim da funcao_01')

def funcao_02():
    print('inicio da funcao-02')
    lista = range(10)
    for i in range(11):
        try:
            print(lista[i])
        except IndexError:
            print('fim da funcao_02')

main()

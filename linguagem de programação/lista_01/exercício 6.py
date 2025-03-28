def verificar_nome(nome:str):
    lista = nome.split()
    primeiro = lista[0]
    print(primeiro)
    print(primeiro.isalpha())
    if primeiro.isalpha():
        return primeiro
    else:
        return "Erro"
print(verificar_nome("Arthur"))
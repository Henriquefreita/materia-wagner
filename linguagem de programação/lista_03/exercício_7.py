def ler_nomes():
    nomes = []
    for i in range(10):
        nome = input(f"Digite o nome da pessoa {i+1}: ")
        nomes.append(nome)
    nome_procurado = input("Digite o nome que você deseja procurar: ")
    if nome_procurado in nomes:
        print("achei ai ")
    else:
        print("achei não ó")
ler_nomes()

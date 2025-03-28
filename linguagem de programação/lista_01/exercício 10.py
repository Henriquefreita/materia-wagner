def lerinformacoes():
    valor = float(input("Digite o valor: "))
    moeda = input("Digite o tipo [R]eal, [D]olar, [E]uro: ")
    return valor, moeda

def converter_moeda(dado):
    valor = dado[0]
    moeda = dado[1]
    real = 0.0
    dolar = 0.0
    euro = 0.0
    if moeda.upper()=="R":
        real = valor
        dolar = valor * 0.17
        euro = valor * 0.16
    if moeda.upper()=="D":
        real = valor * 5.7824
        dolar = valor
        euro = valor * 0.9198
    if moeda.upper()=="E":
        real = valor * 6.2867
        dolar = valor * 0.10872
        euro = valor
    return f'Real: {real:.2f} \n Dólar: {dolar:.2f} \n Euro: {euro:.2f}'
while True:
    print(converter_moeda(lerinformacoes()))
    continuar = input("Continuar? ")
    if continuar == "n":
        break
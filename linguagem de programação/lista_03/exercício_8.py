def temperaturas_acima_da_media():
    temperaturas = []
    for i in range(7):
        temp = float(input(f"Digite a temperatura do dia {i + 1}: "))
        temperaturas.append(temp)
    media = sum(temperaturas) / len(temperaturas)
    dias_acima_da_media = sum(1 for temp in temperaturas if temp > media)
    return dias_acima_da_media
dias_acima = temperaturas_acima_da_media()
print(f"Quantidade de dias com temperatura acima da média: {dias_acima}")

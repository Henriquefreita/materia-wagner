def idade(idade_str):
    try:
        idade = int(idade_str)
        if idade >= 18:
            return "maior de idade."
        else:
            return "menor de idade."
    except ValueError:
        return "Valor inválido"
print(idade("20")) 
print(idade("15")) 
print(idade("abc"))  

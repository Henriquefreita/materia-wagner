def celsius_para_fahrenheit(calculo):
    faherenheint =  (1.8 * calculo) + 32
    return faherenheint    
celsius = int(input("Digite a temperatura: "))
print(celsius_para_fahrenheit(celsius))
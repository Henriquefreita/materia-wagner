x = input('digite uma palavra: ')
quant = len(x) - 1
variavel = ''
for quant in range(quant,-1,-1):
    variavel += x [quant]
print(variavel)
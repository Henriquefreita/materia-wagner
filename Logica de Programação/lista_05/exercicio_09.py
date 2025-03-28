x = input('digite uma palavra: ')
sigla=''
for plv in x.split():
    if plv[0].isupper():
        sigla+=plv[0]
print(sigla)

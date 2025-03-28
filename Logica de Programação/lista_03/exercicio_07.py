pedro = 150
lucas = 110
tempo = 0
while pedro > lucas:
    pedro+=2
    lucas+=1
    tempo+=1
    if pedro == lucas:
        break

print('em',tempo,'anos eles terão a mesma altura')
print('em',tempo+1,'anos lucas será maior que pedro')

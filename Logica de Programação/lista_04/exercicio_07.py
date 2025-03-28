num = int(input('digite 1 numeros: '))
maior = num
menor = num
for n in range(5):
    x = int(input('digite 5 numeros: '))
    if x > maior:
        maior = x
    if x < menor:
        menor = x
print(f'menor = {menor} maior = {maior}')

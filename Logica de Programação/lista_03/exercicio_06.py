soma = 0
conta = 0
while True:
    num = int(input('numero: '))
    if num%2==0:
        break
    soma = soma + num
    conta = conta + 1
    print('soma:', soma)
    print('conta:', conta)
media = soma * conta
print('media: ', media)
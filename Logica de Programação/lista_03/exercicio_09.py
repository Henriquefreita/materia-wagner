num = int(input('digite um numero: '))
fat = num
print('fatorial de ', num, '->', num, end=' ')
while True:
    num = num - 1
    fat = fat * num  
    print('*', num, end='')
    if num ==1:
        break
print(fat)
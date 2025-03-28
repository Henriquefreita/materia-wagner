def ler_numero():

    nums = []
    for i in range(8):
        nums.append(int(input(f'Digire o{i+1}º o numero: ')))
        while True:
            try:
                x = int(input('digite o valor de x : '))
                if x >=0 and x<len(nums):
                    break
            except(ValueError, IndexError):
                print('valor invalido')
        while True:
            try:
                y = int(input('digite o valor de y : '))
                if y >=0 and y<len(nums):
                    break
            except(IndexError, ValueError):
                print('codigo invalido')
            print(nums[x]+nums[y])

ler_numero()
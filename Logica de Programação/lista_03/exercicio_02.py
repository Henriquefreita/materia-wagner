while True:
    numero1 = int(input('escreva um numero: '))
    numero2 = int(input('escreva um numero: '))
    soma = numero1 + numero2
    print(soma)
    sim = input('deseja continuar(sim/não): ')
    if sim == 'nao':
        break

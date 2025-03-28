while True:
    usuário = str(input('nome: '))
    senha = input('senha: ')
    if usuário != 'ALUNO':
        print('usuario incoreto')
    elif senha != 'logic@2024':
        print('senha incorreta')
    else:
        print('Usuário autenticado com sucesso!')
        break 
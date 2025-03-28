def converterhora(hora:str):
    h = hora.split(':')[0]
    m = hora.split(':')[1]
    print(hora.split(':'))
    msg = " "
    if h<="1":
        msg = f'{h} hora'
    else:
        msg = f'{h} horas'
    if m == "1":
        msg += f' e {m} minuto'
    elif m >"1":
        msg += f' e {m} minutos'
    return msg


print(converterhora("12:20"))

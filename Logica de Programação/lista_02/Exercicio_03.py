time1 = str(input('primeiro time: '))
gols1 = int(input('gols do primeiro time: '))
time2 = str(input('segundo time: ', ))
gols2 = int(input('gols do segundo time: '))
if gols1 > gols2 :
    print('vencedor: ', time1)
elif gols2 > gols1 :
    print('vencedor: ', time2)
else :
    print('empate')
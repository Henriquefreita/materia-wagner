x = (list(range(5,501,5)))
for n in (x):
    print(n, end=',')
    if n % 50 == 0:
        print()

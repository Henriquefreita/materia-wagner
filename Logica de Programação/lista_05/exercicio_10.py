x = input("Digite uma palavra: ")
z = ""
for a in x:
    if a.isalnum():
        z += a
print("sem caracteres especiais:", z)
positivos = 0
soma = 0
for i in range(6):
  valor = float(input())
  if valor > 0:
    positivos += 1 
    soma += valor  
if positivos > 0:
  media = soma / positivos
else:
  media = 0
print(positivos)
print(f"{media:.1f}")
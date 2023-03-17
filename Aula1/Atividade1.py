n = str(input("Digite um número inteiro com no máximo 1000 dígitos: "))
lista = []

for i in n:
  lista.append(i)

s = 0
for i in range(len(lista)):
  a = int(lista[i])
  s = s + a

if s % 9 == 0:
  print("true")

else:
  print("false")

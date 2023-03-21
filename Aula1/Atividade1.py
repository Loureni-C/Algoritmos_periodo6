aux = int(input('Digite um numero: '))

a = 1
if aux%9 == 0:
   
  while aux> 9:
  
    aux = sum(int (i) for i in str(aux))
    if aux == 9:
      a = a + 1
      print("igual a 9")
    else:
      a = a + 1
      aux = sum(int (i) for i in str(aux))
  print("True")
 #print(aux)
  print(a)
else:
  print("False")

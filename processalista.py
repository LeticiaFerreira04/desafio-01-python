def maior_impar(lista):
  max = lista[0]
  for item in lista:
    if(item % 2 == 1):
      if(item > max):
        max = item
  print(max)



def menor_impar(lista):
  min = lista[0]
  for item in lista:
    if(item % 2 == 1):
      if(item < min):
        min = item
  print(min)



def maior_menor_impar(lista):
  print("Maior número: ")
  maior_impar(lista)
  print("Menor número: ")
  menor_impar(lista)
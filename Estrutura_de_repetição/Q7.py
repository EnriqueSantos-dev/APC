a=[]


for i in range (5):
	lista=int(input("Digite valores para o conjunto:"))
	a.append(lista)
	
cont = 0 

for i in range(len(a)):
  if a[i] < 0:

      cont += 1 


print("A quantidade de valores negativos presentes no conjunto é igual a:",cont)
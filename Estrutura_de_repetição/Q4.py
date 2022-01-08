n=2
a=[]

for i in range( 4):
	conj=int(input(" Adicione valores para o conjunto:"))
	a.append(conj)


f=0
for x in range(len(a)):
	if a[x] > n:
		f+=1
print("A quantidade de elementos maiores que n é igual a:",f)
	 
		

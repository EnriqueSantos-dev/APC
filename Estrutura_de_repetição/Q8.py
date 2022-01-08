n=int(input("Adicione um valor para N :"))
a=[]
b=[]

for i in range( 4):
	conj=int(input(" Adicione valores para o conjunto:"))
	a.append(conj)


f=0
for x in range(len(a)):
	if a[x] > n:
		b.append(a[x])
		f+=1
print(b)
	 
		

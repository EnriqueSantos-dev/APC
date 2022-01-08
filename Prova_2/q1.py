
lis=[]
for i in range (0,4):
	val=int(input("digite valores: "))
	lis.append(val)


lis2=[]

for i in range (0,4):
	val1=int(input("digite valores lista 2: "))
	lis2.append(val1)


lista=[]
e=len(lis)

for i in range(e):
	lista.append(lis[i])
	lista.append(lis2[i])

print(lista)
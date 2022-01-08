
a=[]
b=[]
p=int(input("digite a quantidade de elementos que vc quer!:"))

for i in range (p):
	x=int(input("Adicione um valor para o cojunto A:"))
	e=int(input("Adicione um valor para o conjunto B:"))
	a.append(x)
	b.append(e)
	
soma=0
for i in range(p):
	formR= ((a[i] - b[i]))**2
	soma+=formR
	
distancia= (soma**0.5)

print(distancia)
	

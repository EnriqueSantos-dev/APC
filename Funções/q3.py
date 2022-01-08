
def maior_soma(a):
	lista_ord=sorted(a)
	print(lista_ord)
	n1=lista_ord[len(lista_ord) -1]
	n2=lista_ord[len(lista_ord) -2]
	soma=n1+n2
	print(f" a soma máxima entre dois elementos é {soma}!")
	
a=[]	
for i in range(0,4):
	val=int(input("digite valores para lista:"))
	a.append(val)
maior_soma(a)




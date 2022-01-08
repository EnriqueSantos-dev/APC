def result_n(lista):
	maxi=max(lista)
	
	a=[]
	i=0
	for en in (lista):
		nota=((lista[i]/maxi)*10)
		a.append(nota)
		i+=1
		a.sort()
	print(f"As notas após a aplicação da fórmula ficaram da seguinte forma \n{a}")
	
lista=[10.0,3.0,8.0,9.0,5.0]
result_n(lista)
	
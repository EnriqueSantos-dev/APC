def nota_result(lista):
	a=[]
	lista=sorted(lista)
	maxi=max(lista)
	mini=min(lista)
	
	i=0
	for en in (lista):
		nota=((lista[i]-mini)/(maxi-mini)*10)
		nota= round(nota,2)
		a.append(nota)
		i+=1
		vma=max(a)
		vme=min(a)
	print(f"As notas após a aplicação da fórmula ficaram da seguinte \n {a}")
	print(f" O aluno com a menor nota que foi: {vme}, logo ficou com 0 na nota final")
	print(f" O aluno com a maior nota que foi {vma}, logo ficou com 10.0 na nota final")
		
	
lista=[7.0,6.0,7.7,2.0,5]

nota_result(lista)
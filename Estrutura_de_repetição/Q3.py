dc =[]
ac = []
soma=0
cont=1
med=0
while cont< 5:
    var= int(input("Insira um valor inteiro para a lista:"))
    dc.append(var)
    cont = (cont+ 1)

print(dc)

soma= sum(dc)
med= (soma / (len(dc)))

cont=0
while cont< 4:
	if (dc[cont]) < med and med!= dc[cont]:
		ac.append((dc[cont]))
	cont = (cont+1)

print("A quantidade de numeros menor que a média é:",len(ac))
dc = []
soma=0
soma2=0
cont=0
while cont< 5:
    var= int(input("Insira um valor inteiro para a lista:"))
    dc.append(var)
    cont = (cont+ 1)

soma1= max(dc)
soma2= min(dc)

amp= soma1- soma2 
print("A amplitude desse conjunto é igual a:", amp)
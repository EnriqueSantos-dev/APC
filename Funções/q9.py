
lista = []
ind=1
for n in range(0,5):
    numeros = int(input(f"Digite o {ind}° valor: "))
    ind+=1
    lista.append(numeros)
#
def med(cnt1):
    media = sum(lista)/len(lista)
    return media
#
def variancia(cnt1):
    media = med(cnt1)
    varian = (((lista[0]-media)**2)+((lista[1]-media)**2)+((lista[2]-media)**2)+((lista[3]-media)**2)+((lista[4]-media)**2))
    return(varian)
print(variancia(""))
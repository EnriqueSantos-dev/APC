
L= 0
slt = (input("Digite uma palavra: "))
slt=slt.lower()
print(slt)

for i in slt:
	if (i== "a" or  i=="e" or i== "i" or i== "o" or i== "u"):
		L+=1
	

print (f"essa palavra|{slt}| tem uma quantidade de vogais igual a :",L)

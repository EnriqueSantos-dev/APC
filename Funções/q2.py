def encontrar_valor(n,list):
	if n in list:
		print(f" o valor {n} está na lista!")
	else:
		print(f"o valor |{n}| não está na lista!" )

n=int(input("adicione o valor que vc quer achar:"))
list=[1,8,9,10,4,8,6]

encontrar_valor(n,list)
	



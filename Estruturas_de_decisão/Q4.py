nome=input("insita o nome:")
valor= float(input("insira o valor devenda:"))
print("O funcionari",nome,"receberá a comição de:")
if valor > 50000:
	print( 0.12* valor)
	
elif valor > 29999 and valor < 50001:
	print(valor*0.095)
else:
	print(valor*0.07)

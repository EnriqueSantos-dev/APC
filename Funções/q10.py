def  conta_caractere(palavra,pal1):
	if pal1 in palavra:
		print(" é um segmento ")
	else:
		print(" não é um segmento   ")

palavra = input("digite a  primeira palavra\n")
palavra=palavra.lower()
pal1=input("digite a segunda palavra \n")
pal1=pal1.lower()


conta_caractere(palavra,pal1)

def  conta_caractere(palavra,pal1):
	if pal1==palavra:
		print("é uma permutação ")
	else:
		print("não é uma permutação   ")

palavra = input("digite a  primeira palavra\n")
palavra=palavra.lower()
palavra=sorted(palavra)
pal1=input("digite a segunda palavra \n")
pal1=pal1.lower()
pal1=sorted(pal1)

conta_caractere(palavra,pal1)
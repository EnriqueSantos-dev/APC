def fn(dici):
	ne=input("\nDigite o seu nome para saber sua media: ")
	ne=ne.lower()
	if ne in dici:
		nota=dici[ne]
		media=(nota[0]+nota[1])/2
		print("{} a sua média é : {:.1f}".format(ne,media))
	else:
		print("\nseu nome não está na lista!")
	




dici={}
q=int(input("Qual a quantidade de alunos?: "))
f=1
for i in range (q):
	nome=input(f"digite seu nome aluno {f}°: ")
	nome=nome.lower()
	f+=1
	if len(nome)>0:
		nota1=float(input("digite a nota 1: "))
		if nota1<0:
			nota1=nota1*(-1)
		if nota1<0:
			nota2=nota2*(-1)
		nota2=float(input("digite a nota 2: "))	
		dici[nome]=nota1,nota2
		print(dici)
		
	else:
		break
		
		
fn(dici)

def incluir_novo(di):
	nome=input("\nQual nome vc quer incluir?:")
	nome=nome.lower()
	di[nome]=nome
	nu=int(input(f"\nQuantos números vc quer adicionar ao contato {nome}?:"))
	f=1
	lista=[]
	for i in range(nu):
		num=input(f"\nDigite o {f}° número: ")
		lista.append(num)
		f+=1
	di[nome]=lista
	di=di
	return (f"\nSua lista atualizada{di}")
		
def incluir_telefone(di):
	a=[]
	dig=input("\nQual o nome do contato que vc quer adicionar mais números?")
	dig=dig.lower()
	if dig in di:
		qua=int(input("\nQuantos numeros vc quer adicionar?"))
		for i in range(qua):
			tel_n=input("Digite os telefones: ")
			a.append(tel_n)
			
		tel=di[dig]+a
		print(tel)
		di[dig]=tel
		di=di
		print(di)
	else:
		print("\nSEU NOME NÃO ESTÁ NA LISTA")
		respo=input("\nVocê gostaria de adicionar esse nome na agenda ?\n RESPONDA sim ou nao!")
		respo.lower()
		if respo=="sim":
			print(incluir_novo(di))
		else:
			print("OK!")

		
def excluir_telefone(di):
	dici={}
	q=input("\nQual o nome da pessoa que vc quer excluir o telefone?:")
	tele=di[q]
	print(f"\n{tele} essse são os telefones de {q} ")
	ex=input("\nDigite o número que vc quer exluir! se o contato tiver só um telefone o nome dele será exlcuido da agenda!!!")
	if ex in tele  and (len(tele) == 1):
		del di[q]
		di=di
		print(di)
	else:
		tele.remove(ex)	
	return di
	
def consultar_telefone(di):
			nome=input("\nQual nome vc quer consultar?")
			nome.lower()
			if nome in di:
				tele=di[nome]
			return (f"\nSeus números {tele}")

			

no=input("Digite o primeiro nome da sua agenda!:\n")
no=no.lower()
nu_q=int(input("\nQuantos números esse contato vai ter?"))
di={}
L=1
list=[]
for i in range(nu_q):
	nume=input(f"\ndigite o {L}° número: ")
	list.append(nume)
	L+=1
di[no]=list
print(f"\nEssa é a sua agenda\n{di}")


print("\nQual função você quer usar?")
print("\nIncluir novo nome? == Digite 1 para escolhe-lá\nIncluir Telefone? == Digite 2 para escolhe-lá\nExcluir telefone? == Digite 3 para escolhe-lá\nCosultar telefone? == Digite 4 para escolhe-lá")

respota=int(input("Digite o valor correspondente a função: "))


lis=[1,2,3,4]
while (respota in lis):
		if respota==1:
			print(incluir_novo(di))
			res=int(input("\nVocê quer usar a função novamente? digite 1 para sim ou  0 para nao!: "))
			if res==1:
				continue
			else:
				res==0
				print("\nQual função você quer usar?")
				print("\nIncluir novo contato? == Digite 1 para escolhe-lá\nIncluir Telefone? == Digite 2 para escolhe-lá\nExcluir telefone? == Digite 3 para escolhe-lá\nCosultar telefone? == Digite 4 para escolhe-lá")
				respota=int(input("Digite o valor correspondente a função: "))
				
		elif respota==2:
			print(incluir_telefone(di))
			res=int(input("\nVocê quer usar a função novamente? digite 1 para sim ou  0 para nao!: "))
			if res==1:
				continue
			else:
				res==0
				print("\nQual função você quer usar?")
				print("\nIncluir novo telefone? == Digite 1 para escolhe-lá\nIncluir Telefone? == Digite 2 para escolhe-lá\nExcluir telefone? == Digite 3 para escolhe-lá\nCosultar telefone? == Digite 4 para escolhe-lá")
				respota=int(input("Digite o valor correspondente a função: "))
			
		elif respota==3:
			print(excluir_telefone(di))
			res=int(input("\nVocê quer usar a função novamente? digite 1 para sim ou  0 para nao!: "))
			if res==1:
				continue
			else:
				res==0
				print("\nQual função você quer usar?")
				print("\nIncluir novo telefone? == Digite 1 para escolhe-lá\nIncluir Telefone? == Digite 2 para escolhe-lá\nExcluir telefone? == Digite 3 para escolhe-lá\nCosultar telefone? == Digite 4 para escolhe-lá")
				respota=int(input("Digite o valor correspondente a função: "))
			
		elif respota==4:
			print(consultar_telefone(di))
			res=int(input("\nVocê quer usar a função novamente? digite 1 para sim ou  0 para nao!: "))
			if res==1:
				continue
			else:
				res==0
				print("\nQual função você quer usar?")
				print("\nIncluir novo telefone? == Digite 1 para escolhe-lá\nIncluir Telefone? == Digite 2 para escolhe-lá\nExcluir telefone? == Digite 3 para escolhe-lá\nCosultar telefone? == Digite 4 para escolhe-lá")
				respota=int(input("Digite o valor correspondente a função: "))
		
			
			
			
while (respota not in list):
		print("\nESSE NÚMERO NÃO CONRRESPONDE A NENHUMA FUNÇÃO!")
		respota=int(input("\nDigite o valor correspondente a função: "))
		if respota==1:
			print(incluir_novo(di))
			res=int(input("\nVocê quer usar a função novamente? digite 1 para sim ou  0 para nao!: "))
			if res==1:
				continue
			else:
				res==0
				print("\nQual função você quer usar?")
				print("\nIncluir novo contato? == Digite 1 para escolhe-lá\nIncluir Telefone? == Digite 2 para escolhe-lá\nExcluir telefone? == Digite 3 para escolhe-lá\nCosultar telefone? == Digite 4 para escolhe-lá")
				respota=int(input("Digite o valor correspondente a função: "))
				
		elif respota==2:
			print(incluir_telefone(di))
			res=int(input("\nVocê quer usar a função novamente? digite 1 para sim ou  0 para nao!: "))
			if res==1:
				continue
			else:
				res==0
				print("\nQual função você quer usar?")
				print("\nIncluir novo telefone? == Digite 1 para escolhe-lá\nIncluir Telefone? == Digite 2 para escolhe-lá\nExcluir telefone? == Digite 3 para escolhe-lá\nCosultar telefone? == Digite 4 para escolhe-lá")
				respota=int(input("Digite o valor correspondente a função: "))
			
		elif respota==3:
			print(excluir_telefone(di))
			res=int(input("\nVocê quer usar a função novamente? digite 1 para sim ou  0 para nao!: "))
			if res==1:
				continue
			else:
				res==0
				print("\nQual função você quer usar?")
				print("\nIncluir novo telefone? == Digite 1 para escolhe-lá\nIncluir Telefone? == Digite 2 para escolhe-lá\nExcluir telefone? == Digite 3 para escolhe-lá\nCosultar telefone? == Digite 4 para escolhe-lá")
				respota=int(input("Digite o valor correspondente a função: "))
			
		elif respota==4:
			print(consultar_telefone(di))
			res=int(input("\nVocê quer usar a função novamente? digite 1 para sim ou  0 para nao!: "))
			if res==1:
				continue
			else:
				res==0
				print("\nQual função você quer usar?")
				print("\nIncluir novo telefone? == Digite 1 para escolhe-lá\nIncluir Telefone? == Digite 2 para escolhe-lá\nExcluir telefone? == Digite 3 para escolhe-lá\nCosultar telefone? == Digite 4 para escolhe-lá")
				respota=int(input("Digite o valor correspondente a função: "))
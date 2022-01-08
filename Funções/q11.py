def validar_CPF(a):
 	
 	rs= ((a[0]*10)+(a[1]*9)+(a[2]*8)+(a[3]*7)+(a[4]*6)+(a[5]*5)+(a[6]*4)+(a[7]*3)+(a[8]*2))
 	digito_1=((rs*10)%11)
 	if digito_1==10:
 		a.append(0)
 	else:
 		a.append(digito_1)

 	cpf_final= ((a[0]*11)+(a[1]*10)+(a[2]*9)+(a[3]*8)+(a[4]*7)+(a[5]*6)+(a[6]*5)+(a[7]*4)+(a[8]*3))+(a[9]*2)
 	digito_2=((cpf_final*10)%11)
 	if digito_2==10:
 		a.append(0)
 	else:
 		a.append(digito_2)
 		if a[8]==1:
 			print("\nSeu CPF foi emitido em um desses Estados:\nDistrito Federal, Goiás, Mato Grosso do Sul ou Tocantins")
 		elif a[8]==2:
 				print("\nSeu CPF foi emitido em um desses Estados:\nPará, Amazonas, Acre, Amapá, Rondônia ou Roraima")
 		elif a[8]==3:
 			print("\nSeu CPF foi emitido em um desses Estados:\nCeará, Maranhão ou Piauí")
 		elif a[8]==4:
 			print("\nSeu CPF foi emitido em um desses Estados:\nPernambuco, Rio Grande do Norte, Paraíba ou Alagoas")
 		elif a[8]==5:
 			print("\nSeu CPF foi emitido em um desses Estados:\nBahia ou Sergipe;")
 		elif a[8]==6:
 			print("\nSeu CPF foi emitido em um desses Estados:\nMinas Gerais")
 		elif a[8]==7:
 			print("\nSeu CPF foi emitido em um desses Estados:\nRio de Janeiro ou Espírito Santo")
 		elif a[8]==8:
 			print("\nSeu CPF foi emitido em um desses Estados:\nSão Paulo")
 		elif a[8]==9:
 			print("\nSeu CPF foi emitido em um desses Estados:\nParaná ou Santa Catarina")
 		else:
 			a[8]==0
 			print("\nSeu CPF foi emitido em um desses Estados:\nRio Grande do Sul")
 
 		
 	print(f"\nSEU CPF VALIDADO É!: {a[0]}{a[1]}{a[2]}.{a[3]}{a[4]}{a[5]}.{a[6]}{a[7]}{a[8]}-{a[9]}{a[10]}")



print("PARA VALIDAR O CPF É NECESSARIO DIGITAR 9 DIGITOS! ENTRE 0 E 9!")

n=1
a=[]
while(len(a)<9):
   cpf = int(input(f"\ndigite o {n}° do seu CPF:"))
   if cpf>9 or cpf<0:
   	n=1
   else:
   	n+=1
   if(cpf<=9) and (cpf>=0):
      a.append(cpf)
   else:
      
      print("\nINCORRETO!!!\nDIGITE UM VALOR POSITIVO  ENTRE 0 E 9!")



validar_CPF(a)



def  conta_caractere(palavra,n):
	result=palavra.count(n)
	print(f"O caractere foi encontrado {result} vez/vezes na palavra :{palavra}: ")

		
palavra=input("digite a palavra:\n")
palavra=palavra.lower()
n=input("digite o caractere que você deseja ver a ocorrência:\n")
n=n.lower()

conta_caractere(palavra,n)

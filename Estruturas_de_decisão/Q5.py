a=int(input("digite um valor para a:"))
b=int(input("digite um valor para b:"))
c=int(input("digite um valor lara c:"))
if( a>b+c) or (b> a+c) or (c>a+b):
	print(" essa forma geométrica não é um triângulo")
else:
	print("essa forma geometrica  é um triangulo")
	if  c == a and a == b and b==c:
		print("esse é um tiângulo equilátero")
	
	elif a != b and b != c and c != a:
		print("esse é um triângulo escaleno")
	elif a==b and a!=c or b==c and b!=a or a==c and a!=b:
	   print ("esse é um triângulo isósceles")
    
	
	
    
    	
	
	

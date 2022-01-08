a=int(input("digite o primeiro número:"))
b=int(input("digite  o segundo número:"))
c=int(input("digite l terceiro número"))
pri=int 
seg=int
ter=int
if(a>b) and (a>c):
	pri=a 
if(b>a)and(b>c):
	pri=b
if(c>a)and(c>b):
	pri=c
if(a<b) and (a<c):
	seg=a 
if(b<a)and(b<c):
	seg=b
if(c<a)and(c<b):
	seg=c
if(a<b) and (a>c) or (a<c) and (a>b):
	ter=a 
if(b<a) and (b>c) or (b<c) and (b>a):
	ter=b
if(c<a) and (c>b) or (c<b) and (c>a):
	ter=c
print (seg)
print(ter)
print(pri)
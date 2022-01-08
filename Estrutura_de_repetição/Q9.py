a = []
min_sub =(2**16)
numb = 0

numb = int(input("Qual o valor que deseja encontrar?: "))
for n in range(0,5):
    numeros = int(input("Digite um valor :"))
    a.append(numeros)
    sub = (abs(a[n]-numb))
    if sub <= min_sub:
        min_sub = sub
        numb = numeros
print("O valor mais próximo é: ",numb)        
        
        


        
    

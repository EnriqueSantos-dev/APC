def veri(a):
    v = int(input("Por qual número deseja multiplicar? "))
    for x in range(0,l1):
        for y in range(0,co):
            multi = matriz[x][y] * v
            matriz[x][y] = multi
    return(matriz)

matriz = []
l1 = int(input("Quantas linhas terão a matriz? "))
for h in range(0,l1):
    matriz.append([])
co = int(input("Quantas colunas terão a matriz? "))
x = 1
y = 1
li_m= l1

for l in range(0,l1):
    for c in range(0,co):
        v = int(input(f"Digite o valor para a {x}° linha {y}° coluna da matriz: "))
        y += 1
        matriz[l].append(v)
        if y > co:
            y = 1
    x += 1

print(veri("a"))
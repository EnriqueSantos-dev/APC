matriz_a = [[0,0],[0,0]]
for l in range(0,2):
    for c in range(0,2):
        matriz_a[l][c] = int(input(f"Digite um valor para (matriz a) [{l}, {c}]: "))

matriz_b = [[0,0],[0,0]]
for l in range(0,2):
    for c in range(0,2):
        matriz_b[l][c] = int(input(f"Digite um valor para (matriz b ) [{l}, {c}]: "))
        
a = (matriz_a[0][0])*(matriz_b[0][0])+(matriz_a[0][1])*(matriz_b[1][0])
b = (matriz_a[0][0])*(matriz_b[0][1])+(matriz_a[0][1])*(matriz_b[1][1])
c = (matriz_a[1][0])*(matriz_b[0][0])+(matriz_a[1][1])*(matriz_b[1][0])
d = (matriz_a[1][0])*(matriz_b[0][1])+(matriz_a[1][1])*(matriz_b[1][1])
matriz_result = [[a,b],[c,d]]
print(matriz_result)
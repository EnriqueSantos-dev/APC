matriz = [[0,0,0],[0,0,0],[0,0,0]]
for x in range(0,3):
    for y in range(0,3):
        matriz[x][y] = int(input(f"Digite o valor para a {x+1}°linha {y+1}° coluna da matriz: \n"))
def quadradinho(a):
    A = (matriz[0][0])+(matriz[1][1])+(matriz[2][2])
    B = (matriz[0][1])+(matriz[0][0])+(matriz[0][2])
    C= (matriz[0][2])+(matriz[1][1])+(matriz[2][0])
    D = (matriz[1][0])+(matriz[1][1])+(matriz[1][2])
    E = (matriz[1][1])+(matriz[0][1])+(matriz[2][1])
    F = (matriz[0][0])+(matriz[1][0])+(matriz[2][0])
    G = (matriz[2][0])+(matriz[2][1])+(matriz[2][2])
    H = (matriz[0][2])+(matriz[1][2])+(matriz[2][2])
    if A == B == C == D == E == F == G == H:
        print("="*24,end=)
        print("É um quadrado perfeito")
        print("="*24)
    else:
        print("="*24)
        print("Não é um quadrado perfeito")
        print("="*24)


quadradinho(matriz)
		
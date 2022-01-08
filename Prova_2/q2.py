di = {}
i = []
u = 1
val = ['nome','preço','desconto','disponibilidade']
for x in range(0,1):
    m = []
    key = int(input(f"Digite o id do produto {u} : "))
    i.append(key)
    for y in range(0,4):
        valo = str(input(f"Digite o nome do produto {val[y]}: "))
        m.append(valo)
    di[key] = m
    u+= 1

for  e in range(0,len(i)):
    a = di[i[e]]
    precofinal = int(a[1]) - int(a[2])
    print(f"O nome do produto {e+1}° é",a[0])
    print(f"O preço (sem desconto) do produto {e+1}° é",a[1])
    print(f"O desconto do produto: {e+1}° é",a[2])
    print(f"O disponibilidade do produto {e+1}° é",a[3])
    print(f"O nome do produto: {e+1}° é",precofinal)
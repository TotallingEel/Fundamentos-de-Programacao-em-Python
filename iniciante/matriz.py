matriz = [
    [1, 2],
    [3, 4]
]

for linha in range(len(matriz)):
    newMatriz = []
    for coluna in range(len(matriz[linha])):
        newMatriz.append(matriz[linha][coluna])   
    print(newMatriz)

soma = 0
for linhaSoma in matriz:
    for elementos in linhaSoma:
        soma += elementos

print(soma)
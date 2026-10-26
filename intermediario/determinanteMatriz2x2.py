
matriz = [
    [2.0, 3.0],
    [1.0, 4.0]
]

diagonal_principal = []
diagonal_secundaria = []

for i in range(len(matriz)):
    diagonal_principal.append(matriz[i][i])
    for j in range(len(matriz)):
        j = len(matriz) - 1 - i
        diagonal_secundaria.append(matriz[i][j])
        break

acumulador_principal = 1
for elemento_principal in diagonal_principal:
    acumulador_principal *= elemento_principal

acumulador_secundario = 1
for elemento_secundario in diagonal_secundaria:
    acumulador_secundario *= elemento_secundario

determinante = acumulador_principal - acumulador_secundario

print(f"Resultado: {determinante}")
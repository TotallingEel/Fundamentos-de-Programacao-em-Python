"""
Autor: TotallingEel711
Linguagem: Python 	
Objetivo: Escalonamento de Matriz (Método de Eliminação de Gauss)
"""

def escalonamento(a):
    
    for i in range(len(a) - 1):
        if a[i][i] == 0:
            for j in range(i, len(a)):
                if a[j][i] != 0:
                    a[i], a[j] = a[j], a[i]
                    break
    
        for j in range(i + 1, len(a)):
            fator = a[j][i] / a[i][i]
            for k in range(len(a)):
                a[j][k] -= fator * a[i][k]

    print(f"Fator: {fator}")
    print()
    print(f"Matriz Escalonada: {a}")

    return a

B = [
        [0, 1, 2, 1],
        [1, 2, 1, 0],
        [2, 1, 0, 1],
        [1, 1, 1, 1]
    ]
    
escalonamento(B)

print()

def troca_linha(a):
    
    for i in range(len(a) - 1):
        if a[i][i] == 0:
            for j in range(i, len(a)):
                if a[j][i] != 0:
                    a[i], a[j] = a[j], a[i]
                    break

    print(f"Troca de Linha: {a}")
    return a

A = [
    [0, 1, 2],
    [0, 0, 3],
    [1, 4, 5]
]

troca = troca_linha(A)
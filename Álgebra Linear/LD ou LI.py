import numpy as np

"""
============================================================================
Autor: TotallingEel711
Instituição: Universidade Federal do Maranhão (UFMA)
Curso: Bacharelado Interdisciplinar em Ciência e Tecnologia (BICT)
Disciplina: Álgebra Linear
Linguagem: Python
Atividade: Construção de Código em Python
Objetivo: Análise algorítmica e estudo da dependência e independência entre vetores 
============================================================================ 
"""

# Código para LD e LI de vetores R3
def nomenclatura(vetores1, vetores2):
    
  XY = vetores1[0] * vetores2[1] == vetores1[1] * vetores2[0]
  YZ = vetores1[1] * vetores2[2] == vetores1[2] * vetores2[1]
  XZ = vetores1[0] * vetores2[2] == vetores1[2] * vetores2[0]
    
  if(XY and YZ and XZ):
    return "L.D"
  else:
    return "L.I" 

A = [2, 4, 6] # A = [x, y, z]
B = [4, 8 , 12]

C = [2, 4, 6]
D = [4, 8, 12]

vetoresAB = [
B[0] - A[0], ## B-A = [4 - 2] = [2]
B[1] - A[1], ## B-A = [8 - 4] = [4]
B[2] - A[2]  ## B-A = [12 - 6] =[6]
]

vetoresCD = [
D[0] - C[0],
D[1] - C[1],
D[2] - C[2]
]

print(f"Resultado: {vetoresAB}")
print(f"Resultado: {vetoresCD}")
print(f"Resultado: {nomenclatura(vetoresAB, vetoresCD)}")

print()

# Código para LD e LI de vetores R3
def nomenclaturaR3(v1, v2, v3):

  matriz = np.array([v1, v2, v3])

  determinante = np.linalg.det(matriz)

  resultado_determinante = np.round(determinante, 1)

  print(f"Determinante: {resultado_determinante}")

  if resultado_determinante == 0:
    return "L.D"
  else:
    return "L.I"

a = [1, 0, 7]
b = [5, 9, 3]
c = [6, 4, 8]

resultado = nomenclaturaR3(a, b, c)

print(f"Resultado: {resultado}")
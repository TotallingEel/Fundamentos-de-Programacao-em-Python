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

def entradaR3():
  i = 0
  j = 0

  u = []
  v = []

  print("Digite as componentes do primeiro vetor: ")
  while i != 3:

    u.append(float(input(f"Componente {i+1}: ")))
    i += 1

  print()

  print("Digite as componentes do segundo vetor: ")
  while j !=3:

    v.append(float(input(f"Componente {j+1}: ")))
    j += 1

  return u, v

print()

def nomenclatura(vetores1, vetores2):

  for i, u in enumerate(vetores1, start = 0):
    print(f"{i}. {u}")

  print()

  for j, v in enumerate(vetores2, start = 0):
    print(f"{j}. {v}")

  XY = vetores1[0] * vetores2[1] == vetores1[1] * vetores2[0]
  YZ = vetores1[1] * vetores2[2] == vetores1[2] * vetores2[1]
  XZ = vetores1[0] * vetores2[2] == vetores1[2] * vetores2[0]
    
  if(XY and YZ and XZ):
    return "L.D"
  else:
    return "L.I" 

u, v = entradaR3()
print(f"Resultado: {nomenclatura(u, v)}")

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

a = []
b = []
c = []

contador1 = 0
contador2 = 0
contador3 = 0

print("Digite as componentes do primeiro vetor: ")
while contador1 != 3:

  a.append(float(input(f"Componente {contador1 + 1}: ")))
  contador1 += 1

print()

print("Digite as componentes do segundo vetor: ")
while contador2 !=3:

  b.append(float(input(f"Componente {contador2 + 1}: ")))
  contador2 += 1

print()

print("Digite as componentes do terceiro vetor: ")
while contador3 != 3:

  c.append(float(input(f"Componente {contador3 + 1}: ")))
  contador3 += 1

print()

resultado = nomenclaturaR3(a, b, c)

print(f"Resultado: {resultado}")
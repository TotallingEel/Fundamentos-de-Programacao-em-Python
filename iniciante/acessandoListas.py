computador = ["placa-mãe", "processador", "memória ram", "armazenamento", "placa de vídeo"]

tamanho = len(computador)

for i in range(len(computador)):
  print(f"{i}. {computador[i]}")


print()

i = 0
while i < tamanho:
  print(f"{i}. {computador[i]}")
  i += 1
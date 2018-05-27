from random import randint

matriz = []
t = 5

lmaior = lmenor = cmaior = cmenor = 0
maior = menor = 0

for i in range(t):
    linha = []
    for j in range(t):
        linha.append(randint(1,99))
    matriz.append(linha)

for i in range(t):
    for j in range(t):
        print(matriz[i][j], end=" ")
    print()

for i in range(t):
    for j in range(t):
        if matriz[i][j] > maior:
            maior = matriz[i][j]
            lmaior = i
            cmaior = j

print("\nPosição do maior (%d) elemento: linha %d e coluna %d" % (maior, lmaior+1, cmaior+1))

menor = maior
for i in range(t):
    for j in range(t):
        if matriz[i][j] < menor:
            menor = matriz[i][j]
            lmenor = i
            cmenor = j

print("Posição do menor (%d) elemento: linha %d e coluna %d" % (menor, lmenor+1, cmenor+1))
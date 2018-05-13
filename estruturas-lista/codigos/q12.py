import random

m = []

t = int(input("Tamanho da matrix NxN: "))

#PREENCHE ALEATÓRIAMENTE
for i in range(t):
    linha = []
    for j in range(t):
        num = random.randint(10,20)
        linha.append(num)
    m.append(linha)
print()

i = j = 0
#DIAGONAL PRINCIPAL
dp = 0
for i in range(t):
    for j in range(t):
        if i == j:
            dp = dp + m[i][j]

i = j = 0
#DIAGONAL SECUNDÁRIA
ds = 0
for i in range(t):
    for j in range(t):
        if i == t - 1 -j:
            ds = ds + m[i][j]

maior_linha = 0
maior_coluna = 0
maior = m[0][0]
for l in range(t):
    for c in range(t):        
        if maior < m[l][c]:
            maior = m[l][c]
            maior_linha = l
            maior_coluna = c

i = j = 0
#EXIBE
for i in range(t):
    print("|", end=" ")
    for j in range(t):
        print(m[i][j], end=" | ")
    print()

print("\nSoma da D. Principal com D. Secundária: ", dp+ds)
print("Maior elemento: ", m[maior_linha][maior_coluna])
#print("linha do maior: %d\ncoluna do maior: %d" % (maior_linha+1, maior_coluna+1))

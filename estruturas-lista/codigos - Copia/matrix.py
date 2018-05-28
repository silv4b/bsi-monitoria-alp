m = []
t=4
for i in range(t):
    linha = []
    for j in range(t):
        linha.append(0)
    m.append(linha)

i = j = 0 

for i in range(4):
    print("|", end=" ")
    for j in range(4):
        print(m[i][j], end=" | ")
    print()

i = j = 0

for i in range(4):
    for j in range(4):
        if i == j:
            m[i][j] = 1

print()

for i in range(4):
    for j in range(4):
        if i == t - 1 -j:
            m[i][j] = 2

print()

i = j = 0 

for i in range(4):
    print("|", end=" ")
    for j in range(4):
        print(m[i][j], end=" | ")
    print()

print()

maior_linha = 0
maior_coluna = 0
maior = m[0][0]
for l in range(4):
    for c in range(4):        
        if maior < m[l][c]:
            maior = m[l][c]
            maior_linha = l
            maior_coluna = c

print('O maior elemento é: {}'.format(maior))
print('linha do maior: {}\ncoluna do maior: {}'.format(maior_linha+1, maior_coluna+1))
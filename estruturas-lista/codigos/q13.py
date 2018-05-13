m = []

t = int(input("Tamanho da matrix NxN: "))
t2 = 0

#PREENCHE ALEATÓRIAMENTE
for i in range(t):
    linha = []
    for j in range(t):
        num = 0
        linha.append(num)
    m.append(linha)
print()

i = j = 0
#EXIBE
for i in range(t):
    print("|", end=" ")
    for j in range(t):
        print(m[i][j], end=" | ")
    print()
print()

if(t%2 == 1):
    
    t2 = (t//2)
    m[t2][t2] = 1

    i = j = 0
    #EXIBE
    for i in range(t):
        print("|", end=" ")
        for j in range(t):
            print(m[i][j], end=" | ")
        print()

elif(t%2 == 0):

    l = (t//2)-1
    c = l
    
    m[l][c] = 1
    m[l+1][c] = 1

    m[l][c+1] = 1
    m[l+1][c+1] = 1

    i = j = 0
    #EXIBE
    for i in range(t):
        print("|", end=" ")
        for j in range(t):
            print(m[i][j], end=" | ")
        print()
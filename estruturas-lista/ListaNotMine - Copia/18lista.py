m = []

t = int(input("Tamanho da matrix NxN: "))
t2 = 0

#PREENCHE MATRIZ
for i in range(t):
    linha = []
    for j in range(t):
        num = '-'
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

#SE IMPAR 
if(t%2 == 1):
    
    #(MEIO = 1)
    t2 = (t//2)
    m[t2][t2] = 1

    i = j = 0
    #EXIBE
    for i in range(t):
        print("|", end=" ")
        for j in range(t):
            print(m[i][j], end=" | ")
        print()

#SE IMPAR
elif(t%2 == 0):

    #METADE ESQUERDA CONTADA
    l = (t//2)-1
    c = l
    
    #PREENCHER METADE ESQUERDA
    m[l][c] = 1
    m[l+1][c] = 1

    #PREENCHER METADE DIREITA
    m[l][c+1] = 1
    m[l+1][c+1] = 1

    i = j = 0
    #EXIBE
    for i in range(t):
        print("|", end=" ")
        for j in range(t):
            print(m[i][j], end=" | ")
        print()
import random

m = []
t = 3

for i in range(t):
    l = []
    for j in range(t):
        l.append(random.randint(1,2))
        #l.append(1)
    m.append(l)

#verifica diagonal principal
vdp = 0
#diagonal principal
for e in range(t):
    for g in range(t):
        if e == g:
            vdp += m[e][g]

print("\nDiagonal Pri.:",vdp)

#verifica diagonal secundaria
vds = 0
for e in range(t):
    for g in range(t):
        if e == t - 1 - g:
            vds += m[e][g]

print("Diagonal Sec.:", vds)

#verificação de linhas
vlx1 = vlx2 = vlx3 = 0
for e in range(t):
    for g in range(t):
        #linha 1
        if e == 0:
            vlx1 += m[e][g]
        #linha 2 
        if e == 1:
            vlx2 += m[e][g]
        #linha 3
        if e == 2:
            vlx3 += m[e][g]

print("\nLinhas:",vlx1,vlx2,vlx3)

vcx1 = vcx2 = vcx3 = 0
for e in range(t):
    for g in range(t):
        #linha 1
        if g == 0:
            vcx1 += m[e][g]
        #linha 2 
        if g == 1:
            vcx2 += m[e][g]
        #linha 3
        if g == 2:
            vcx3 += m[e][g]

print("Colunas:", vcx1,vcx2,vcx3)

#visualiza velha
print("\nMATRIZ\n")
print("  ", end="")
for i in range(t):
    print(i+1, end=" ")
print()
for e in range(t):
    print(e+1, end=" ")
    for g in range(t):
        if m[e][g] == 1:
            print('x', end=" ")
        else:
            print('o', end=" ")
    print()
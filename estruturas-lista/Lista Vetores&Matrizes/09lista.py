from random import randint

o = int(input("Ordem: "))
s = 0
m = []
maior = 0
menor = 0

for i in range(o):
    l = []
    for e in range(o):
        if( i == e):
            n = randint(1, 100)
            s += n
            l.append(n)
        else:
            n = randint(1, 100)
            l.append(n)
    m.append(l)

    for g in range(o):
        if(m[i][g] > maior):
            maior = m[i][g]
    
    menor = maior
    for g in range(o):
        if(m[i][g] < menor):
            menor = m[i][g]

for e in range(o):
    print(m[e])

print("\nSoma diagonal P:", s)
print("Maior:", maior)
print("Menor", menor)

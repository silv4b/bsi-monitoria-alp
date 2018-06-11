from random import randint

m = []
n = 5
maior = 0
linha = coluna = 0

for i in range(n):
    l = []
    for e in range(n):
        l.append(randint(1,99))
    m.append(l)

for i in range(n):
    print(m[i])

for i in range(n):
    for g in range(n):
        if(m[i][g] > maior):
            maior = m[i][g]
            linha = i+1
            coluna = g+1
      
print("Lin and Col max: Coluna %d e Linha %d" % (linha, coluna))
    
menor = maior
for i in range(n):
    for g in range(n):
        if(m[i][g] < menor):
            menor = m[i][g]
            linha = i+1
            coluna = g+1

print("Lin and Col min: Coluna %d e Linha %d" % (linha, coluna))

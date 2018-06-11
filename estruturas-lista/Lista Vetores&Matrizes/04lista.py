l = [9,1,3,2,5,2,5,5,7,0,4,1,6,5,9]
t = len(l)
soma = 0

for e in range(t):
    soma += l[e]

print("S0ma: ", soma)

for i in range(t):
    for j in range(t-1):
        if(l[j] > l[j+1]):
            aux = l[j]
            l[j] = l[j+1]
            l[j+1] = aux

print(l)

soma = (l[0] + l[1] + l[2]) + (l[t-1] + l[t-2] + l[t-3])

print("Soma dos 3 maiores com 3 menores: ", soma)
l = []
t = 10

for i in range(t):
    n = int(input("numero: "))
    while n == 0 or (n%2 != 0 and n >= 0):
        n = int(input("inválido -> numero: "))
    l.append(n)

print(l)

for i in range(t):
    for j in range(t-1):
        if(l[j]>l[j+1]):
            aux = l[j]
            l[j] = l[j+1]
            l[j+1] = aux

print(l)
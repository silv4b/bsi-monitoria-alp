L = []
Li = []
T = 10
for i in range(T):
    n = int(input("%d º número: " % (i+1)))
    L.append(n)
print(L)
c = len(L)-1
while c > 0:
    Li.append(L[c])
    c -= 1
print(Li)
for i in range(T):
    for j in range(T-1):
        if L[j] > L[j+1]:
            aux = L[j]
            L[j] = L[j+1]
            L[j+1] = aux
print(L)
for i in range(T):
    for j in range(T-1+(i-i)):
        if L[j] < L[j+1]:
            aux = L[j]
            L[j] = L[j+1]
            L[j+1] = aux
print(L)
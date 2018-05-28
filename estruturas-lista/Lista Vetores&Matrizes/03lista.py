from random import randint

l = []
t = 10

for i in range(t):
    n = randint(1,99)
    l.append(n)

for i in range(t):
    print(l[i], end=" ")
print()

c = t-1

while c >= 0:
    print(l[c], end=" ")
    c -= 1
print()

for i in range(t):
    for j in range(t-1):
        if(l[j] > l[j+1]):
            aux = l[j]
            l[j] = l[j+1]
            l[j+1] = aux

for i in range(t):
    print(l[i], end=" ")
print()

for i in range(t):
    for j in range(t-1):
        if(l[j] > l[j+1]):
            aux = l[j]
            l[j] = l[j+1]
            l[j+1] = aux

c = t-1

while c >= 0:
    print(l[c], end=" ")
    c -= 1
print()
from random import randint

l = []
o = []
t = 10
m = 0

for e in range(t):
    n = randint(-99, 100)
    while n < 0 or n in l:
        print("%d é negativo ou ja existe na lista" % n)
        n = randint(-99, 99)
    m += n
    l.append(n)

print(l)
md = (sum(l)/t)

for i in range(t):
    for e in range(t-1):
        if l[e] > l[e+1]:
            aux = l[e]
            l[e] = l[e+1]
            l[e+1] = aux

print(l)
print("Média:", md)

for i in range(t):
    if l[i] > md:
        print(l[i], end=" ")

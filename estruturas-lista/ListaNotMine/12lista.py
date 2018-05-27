m = int(input("Ordem M: "))
n = int(input("Ordem N: "))
s = int(input("Sequence: "))
t = []

for i in range(m):
    l = []
    for e in range(n):
        l.append(s)
        s += 1
    t.append(l)

for e in range(m):
    print(t[e])
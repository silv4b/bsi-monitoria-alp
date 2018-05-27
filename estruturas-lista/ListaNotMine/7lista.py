o = int(input("Ordem: "))
m = []

for i in range(o):
    l = []
    for i in range(o):
        l.append(0)
    m.append(l)

for e in range(o):
    print(m[e])

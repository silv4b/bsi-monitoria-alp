o = int(input("Ordem: "))
m = []

for i in range(o):
    l = []
    for e in range(o):
        if( i == e):
            l.append(1)
        else:
            l.append(0)
    m.append(l)

for e in range(o):
    print(m[e])

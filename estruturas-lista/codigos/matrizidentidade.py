m = []
n = int(input("Orden: "))

for i in range(n):
    l = []
    for j in range(n):
        if i == j:
            l.append(1)
        else:
            l.append(0)
    m.append(l)

print()
for e in range(len(m)):
    print("|", end=" ")
    for k in range(len(m)):
        print(m[e][k],"|", end=" ")
    print()
print()
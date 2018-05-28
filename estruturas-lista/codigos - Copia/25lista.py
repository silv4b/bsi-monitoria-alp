p = input("Palavra: ")
l1 = []
l2 = []
for i in range(len(p)):
    l1.append(p[i])

print(l1)

c = len(l1)-1

while c >= 0:
    l2.append(l1[c])
    c = c -1

print(l2)

if l1 == l2:
    print("\nPALINDROMA")
else:
    print("\nNÃO PALINDROMA")
p = input("Palavra: ")
l = []
for i in range(len(p)):
    if p[i] != 'a' and p[i] != 'b':
        l.append(p[i])
print(l)
palavra = input("Palavra: ")
l = []

c = len(palavra)-1

while c >= 0:
    l.append(palavra[c])
    c -= 1

print(l)
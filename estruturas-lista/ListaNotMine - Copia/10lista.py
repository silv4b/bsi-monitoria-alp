from random import randint

n = int(input("Quantidade de números: "))

i = []
p = []

for k in range(n):
    o = randint(1, 99)
    if(o%2 == 0):
        p.append(o)
    else:
        i.append(o)

print("Par:", p)
print("Ímpar:", i)

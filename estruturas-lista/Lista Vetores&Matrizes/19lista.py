from random import randint

l = []
t = 10
m = int(input("Mult: "))

for i in range(t):
    l.append(randint(1,100))
print(l)
for e in range(t):
    if l[e] % m == 0:
        print(l[e])
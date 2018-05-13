from random import randint

N = int(input("Os multiplos de: "))
T = int(input("Tamanho da lista: "))
print()

L = []

for i in range(T):
    num = randint(0,100)
    L.append(num)

for i in (L):
    if (i == 0):
        continue
    elif (i % N == 0):
        print (i)
    else:
        continue
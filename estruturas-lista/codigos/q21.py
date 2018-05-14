import random

pares = []
impares = []

n = int(input("Número de elementos: "))

for e in range(n):
    o = random.randint(1,50)    
    if(o%2 == 0):
        pares.append(o)
    else:
        impares.append(o)

print("Pares:", end=" ")
for j in range(len(pares)):
    print(pares[j], end=" ")    

print("\nImpares:", end=" ")
for j in range(len(impares)):
    print(impares[j], end=" ")
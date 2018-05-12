import random

tamanho = 10
L = []*tamanho

for i in range (tamanho):
    dado = random.randint(1,6)
    L.append(dado)

print("\nNumeros sorteados: ", end=" ")
for j in range (tamanho):
    print(L[j], end=" ")

print("\n\nCom funcs:\nMaior número: ", max(L))
print("Menor número: ", min(L))

menor = maior = L[0]
for i in range(tamanho):
    if(L[i] < menor):
        menor = L[i]
    if(L[i] > maior):
        maior = L[i]

print("\nSem funcs:\nMaior número: ", maior)
print("Menor número: ", menor)
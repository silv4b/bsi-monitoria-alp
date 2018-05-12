import random

tamanho = 10
L = []*tamanho

for i in range (tamanho):
    num = random.randint(0, 100)

    '''
    num = int(input("Digite o número: "))
    while num%2 == 1:
        num = int(input("Entrada iválida\nDigite p número: "))
    '''

    L.append(num)
    
print("lista: ", end=" ")
for j in range (tamanho):
    print(L[j], end=" ")

while tamanho > 1:
     trocou = False
     x = 0
     while x < (tamanho-1):
         if L[x] > L[x+1]:
               trocou = True
               temp = L[x]
               L[x] = L[x+1]
               L[x+1] = temp
         x += 1
     if not trocou:
         break
     tamanho -= 1

print("\nlista: ", end=" ")
for e in L:
     print(e, end = " ")
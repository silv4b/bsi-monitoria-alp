L  = [9,1,3,2,5,2,5,5,7,0,4,1,6,5,9]
#print(L)

sum = 0
aux = 0
rst = 0
cnt = len(L)-2
tamanho = tam = len(L)

for i in range(len(L)):
    sum = sum + L[i]

print("\nSoma da esq p/ dir:", sum)

rst = L[cnt] - L[cnt-1]
while cnt > 1:
    rst = rst - L[cnt]
    cnt = cnt -1

print("Subt da dir p/ esq:", rst)

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

#print(L)
print("\nTrês maiores: ", L[tam-1], L[tam-2], L[tam-3])
print("Soma dos três maiores:", (L[tam-1]+L[tam-2]+L[tam-3]))

print("\nTrês menores: ",L[0], L[1], L[2])
print("Soma dos três menores:", (L[0]+L[1]+L[2]))

s1 = (L[tam-1]+L[tam-2]+L[tam-3])
s2 = (L[0]+L[1]+L[2])

print("\nSoma das somas: ", s1+s2)
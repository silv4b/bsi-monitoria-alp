L = []
tamanho = 10

for i in range (tamanho):
    num = int(input("Digite o número: "))
    while num%2 == 1 or num == 0:
        num = int(input("Entrada iválida\nDigite p número: "))
    L.append(num)
    
print("lista: ", end=" ")
for j in range (tamanho):
    print(L[j], end=" ")
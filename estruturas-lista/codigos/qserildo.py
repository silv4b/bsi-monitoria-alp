par = []
impar = []
b = True
v = input("P/ finalizar, digite \"s\":")

if v == 's' or v == 'S':
    b = True

else:
    while b == True:
        n = int(input("Dig. Número: "))
        if n%2 == 0:
            par.append(n)
        else:
            impar.append(n)
        
        v = input("Sair? (S p/ sim, qq coisa p/ não): ")
        if v == 's' or v == 'S':
            b = False

print("lista pares: ", par)
print("lista impares: ", impar)
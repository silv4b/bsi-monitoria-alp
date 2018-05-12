numeros = []

for i in range(10):
    n = int(input("Número: "))
    while (n < 0):
        n = int(input("Entrada incorreta\nNúmero: "))
    while n in numeros:
        n = int(input("Já existe\nNúmero: "))
    numeros.append(n)

print(numeros)
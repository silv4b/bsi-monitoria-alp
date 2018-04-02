
num = int(input("Número: "))
while (num < 0):
    if (num < 0):
        print("Inteiro positivo!")
        num = int(input("Número: "))

print("\nNúmeros pares")
for i in range(1, num+1):
    if (i%2 == 0):
        print(i)

print("\nNúmeros ímpares")
for i in range(0,num+1):
    if (i%2 != 0):
        print(i)
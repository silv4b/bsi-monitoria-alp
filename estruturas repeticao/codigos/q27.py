numero = 1
par = impar = 0

while numero != 0:
    numero = int(input("Digite um numero: "))
    if (numero < 0):
        print("Número não pode ser negativo.")
        numero = int(input("Digite um novo numero: "))
    elif (numero != 0):
        if(numero % 2 == 0):
            par += 1
        else:
            impar += 1

print("Voce digitou {} números pares e {} números ímpares".format(par, impar))
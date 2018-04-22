numero = int(input("\nVoce quer o fatorial de qual termo: "))
fatorial = 1

while (numero < 0):
    print ("O termo deve ser positivo!")
    numero = int(input("\nVoce quer o fatorial de qual termo: "))        

if (numero == 0):
    print("Fatorial de 0 é 1")

else:
    while (numero > 0):
        fatorial = fatorial * numero
        numero = numero - 1

    print(fatorial)
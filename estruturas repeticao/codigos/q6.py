termo = int(input("\nVoce quer o fatorial de qual termo: "))

while (termo < 0):
    print ("O termo deve ser positivo!")
    termo = int(input("\nVoce quer o fatorial de qual termo: "))        

if (termo == 0):
    print("Fatorial de 0 é 1")

else:
    fatorial = 1
    print("\nCom for!")
    for i in range(1, termo + 1):
        fatorial *= i
        print (fatorial)
    
    fatorial = 1
    contador = 1
    print("\nCom while!")
    while(contador <= termo):
        fatorial *= contador
        print (fatorial)
        contador += 1    
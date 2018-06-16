from time import sleep

n1 = int(input("Numero 1: "))
n2 = int(input("Numero 2: "))
opc = 0

while (opc != '0'):

    print('''
    [1] Soma
    [2] Subitração
    [3] Multiplicação
    [4] Divisão
    [5] Atualizar números
    [0] Sair
    ''')

    opc = input("Opção: ")

    if  (opc == '1'):
        print("\n%d + %d = %d" % (n1,n2,n1+n2))
    elif(opc == '2'):
        print("\n%d - %d = %d" % (n1, n2, n1 - n2))
    elif(opc == '3'):
        print("\n%d * %d = %d" % (n1, n2, n1 * n2))
    elif(opc == '4'):
        if(n2 != 0):
            print("\n%d / %d = %d" % (n1, n2, n1/n2))
        else:
            print("\nNão dividirás por 0")
    elif(opc == '5'):
        n1 = int(input("\nNovo número 1: "))
        n2 = int(input("Novo número 2: "))
    elif(opc == '0'):
        print("\nSaindo...")
        sleep(1)
    else:
        print("\nOpção inválida!")
        continue


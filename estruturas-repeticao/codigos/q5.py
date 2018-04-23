# coding: utf-8

num = int(input("Digite um número: "))

cont = num

while cont != 2:
    cont -= 1
    #print(cont)
    if num % cont == 0:
        print("%d não é um número primo!" % num)
        num = int(input("Digite um número primo: "))
        cont = num

print("Número %d é primo\nFIM!" % num)
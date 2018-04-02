soma = 0
numero = int(input("Número: "))
maior = menor = contador = 0

if(numero != 999):
    if (numero < 0):
        print("Número não pode ser negativo.")
        numero = int(input("Digite um numero: "))
    
    soma += numero
    maior = menor = numero
    while (numero != 999):
        numero = int(input("Número: "))
        contador += 1
        if(numero != 999):
            soma += numero
            if(numero > maior):
                maior = numero
            if(numero < menor):
                menor = numero

media = soma/contador
print("\nMaior número: {}\nMenor número: {}".format(maior, menor))
print("Média dos números digitados: {}".format(media))
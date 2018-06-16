base = int(input("Digite o valor da base: "))
expoente = int(input("Digite o valor do expoente: "))

potencia = 1
iteracao = 0
while iteracao < expoente:
    potencia = potencia * base
    iteracao = iteracao + 1

print("%d no expoente %d é: %d" % (base, expoente, potencia))
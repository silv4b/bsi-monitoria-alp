#numero perfeitos 2 - só até o quarto

inicio = int(input("Inicio: "))
fim = int(input("Fim: "))

contador = 0

for contador in range(inicio, fim):
    
    dobro = inicio * 2
    numerot = 0

    for i in range (1, inicio + 1):
        if (inicio % i == 0):
            numerot = numerot + i

    if (numerot == dobro):
        print("\n%d é perfeito" % inicio)

    inicio = inicio + 1
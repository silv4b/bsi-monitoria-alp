#numero perfeitos 2 - só até o quarto
import time as tempo

ini = int(input("Inicio: "))
fim = int(input("Fim: "))
contador = 0

start = tempo.time()

while (contador <= fim):

    num = ini
    numd = num * 2
    cnum = 0

    for i in range (1, num + 1):
        if (num % i == 0):
            cnum = cnum + i

    if (cnum == numd):
        print("\n%d é perfeito" % num)

    ini = ini + 1
    contador = contador + 1

end = tempo.time()

total = end - start

print("Tempo decorrido: %.2f " % total)
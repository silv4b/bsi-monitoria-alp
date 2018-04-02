import random

ini = int(input("Inicio do intervalo: "))
fim = int(input("Fim do intervalo: "))

tnt = 0
r = random.randint(ini, fim)

gess = int(input("Tentativa: "))
while True:
    if(gess == r):
        tnt =+ 1
        print("\nParabéns o numero sorteado foi o %d!?" % gess)
        break
    else:
        tnt =+ 1
        print("Não foi dessa vez, diz outro ai!")
        gess = int(input("Tentativa: "))
print("FIm!")
print("Número de tentativas: %d" % tnt)
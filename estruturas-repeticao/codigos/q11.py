import random

vezes = int(input("Número de rodadas: "))
numero = random.randint(0,3)

if(vezes%2 == 1):
    vezes += 1

for i in range(vezes):
    tentativas = i
    guess = int(input("palpite: "))
    
    if(guess == numero):
        if(tentativas == 1):
            print("Parabéns, vc acertou o número %d em uma tentativa!" % (numero))
        else:
            print("Parabéns, vc acertou o número %d em %d tentativas!" % (numero, tentativas))
        break
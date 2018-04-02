from time import sleep
from os import system as sys #opcional

sys("cls")
tempo = int(input("\n\n\t\tEntrada em horas: "))

#diminui por minuto
for hora in range(tempo -1, -1, -1):
    #diminui pro segundo
    for minuto in range(59, -1, -1):
        for segundo in range(59, -1, -1):
            #limpa a tela
            sys("cls")
            #imprime na tela
            print("\n\n\t\tRestam: %02d:%02d:%02d" % (hora, minuto, segundo))
            #passagem do segundo
            sleep(1)
from time import sleep
from os import system as sys #opcional

sys("cls")
tempo = int(input("\n\n\t\tEntrada em horas: "))

#diminui por hora
for hora in range(tempo -1, -1, -1):
    #diminui por minuto
    for minuto in range(59, -1, -1):
        #diminui por segundo
        for segundo in range(59, -1, -1):
            #limpa a tela
            sys("cls")
            #imprime na tela
            print("\n\n\t\tRestam: %02d:%02d:%02d" % (hora, minuto, segundo))
            #passagem do segundo
            sleep(1)
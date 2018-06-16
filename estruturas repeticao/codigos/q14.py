#votação

cd1 = cd2 = cd3 = cd4 = cd5 = 0
voto = -1
rodadas = 0

while (voto != 0):
    
    rodadas = rodadas + 1
    voto = int(input("Em qual dos 5 candidadotos você irá votar? \nopção (0 para encerrar): "))
    
    if (voto >= 6):
        rodadas -= 1
        print("Canditato inválido")
        voto = int(input("Em qual dos 5 candidadotos você irá votar? \nopção (0 para encerrar): "))
    elif (voto == 1):
        cd1 = cd1 + 1
    elif (voto == 2):
        cd2 = cd2 + 1
    elif (voto == 3):
        cd3 = cd3 + 1
    elif (voto == 4):
        cd4 = cd4 + 1
    elif (voto == 5):
        cd5 = cd5 + 1
    elif (voto == 0):
        break      

print("Rodadas: %d" % rodadas)
print("Média de todos os votos de cada candidado pelo total de %d rodadas" % rodadas)
print("Candidato 1 com %d votos: %.2f" %(cd1, cd1/rodadas))
print("Candidato 2 com %d votos: %.2f" %(cd2, cd2/rodadas))
print("Candidato 3 com %d votos: %.2f" %(cd3, cd3/rodadas))
print("Candidato 4 com %d votos: %.2f" %(cd4, cd4/rodadas))
print("Candidato 5 com %d votos: %.2f" %(cd5, cd5/rodadas))
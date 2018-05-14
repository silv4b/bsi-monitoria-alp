L = []
n = int(input("Número de candidatos: "))
rodada = 0
turno = 2

#ADICIONAR CANDITATOS
for e in range(n):
    candidato = []
    nome = input("Candidato: ")
    id = e+1
    candidato.append(id)
    candidato.append(nome)
    candidato.append(0)
    L.append(candidato)

print()

#VOTAÇÃO

print("CANDIDATOS:\n")
for k in range(len(L)):
    print("ID:", L[k][0], end=" ")
    print("CANDIDATO:", L[k][1])

for m in range(turno):
    contador = True
    print("TURNO: ", m+1)
    while contador == True:
        t = int(input("Em quam Cand. deseja votar (0 p/ sair): "))
        if t == 0:
            break    
        t = t - 1
        L[t][2] = L[t][2] + 1

print("\nDADOS DA VOTAÇÂO")
for q in range(len(L)):
    print("\nId: %d\nNome: %s \nNº Votos: %d\nMédia: %.2f" % (L[q][0], L[q][1], L[q][2], (L[q][2] / turno)))

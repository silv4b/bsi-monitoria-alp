candidatos = [22,45,78,5,45,63,99,2,51,8]
aprovados  = []
em_espera  = []

for i in range(len(candidatos)):
    if (candidatos[i]%2==0):
        #print("aprovado")
        aprovados.append(candidatos[i]) #insere na lista de aprovados
    else:
        #print("lista de espera")
        em_espera.append(candidatos[i]) #insere na lista de espera
    


print("\nAprovados: ", end=" ")
for j in range (len(aprovados)):
    print(aprovados[j], end=" ")

print("\nEm espera: ", end=" ")
for j in range (len(em_espera)):
    print(em_espera[j], end=" ")

print("\n\nQuem não estiver nas listas, foi reprovado")

print("FIM!")
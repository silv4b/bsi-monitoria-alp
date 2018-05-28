candidatos = [22,45,78,5,45,63,99,2,51,8]
aprovados = []
em_espera = []
for i in range(len(candidatos)):
    if candidatos[i]%2 == 0:
        print("aprovado")
        aprovados.append(candidatos[i]) #insere na lista de aprovados
    elif candidatos[i] > 20:
        print ("lista de espera")
        em_espera.append(candidatos[i]) #insere na lista de espera
    else:
        print ("quem não estiver nas listas, foi reprovado")
print("FIM!")

print(aprovados)
print(em_espera)
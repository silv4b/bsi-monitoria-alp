provedores = ["Provedor 1", "Provedor 2", "Provedor 3", "Provedor 4", "Provedor 5"]
taxaSegundo = [0.3, 1.0, 7.0, 9.3, 5.0]

print("\nComparativo de taxa de provedores\n")

for i in range(len(provedores)):
    print("Empresa: ", (i+1))
    print("Nome: ", provedores[i])
    print("Taxa: ", taxaSegundo[i], "mb/s\n")
    i = i + 1

print("Relatorio Final\n")

max = 0
maxIndice = 0

for i in range(len(provedores)):
    print("%d| %s: %.2f mb/s" % (i+1, provedores[i], taxaSegundo[i]))
    if taxaSegundo[i] > max:
        max = taxaSegundo[i]
        maxIndice = i
    i = i + 1

print("\nO provedor com  melhor taxa é o %s" % provedores[maxIndice])

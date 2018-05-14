provedores = []
taxaSegundo = []

quantidade = int(input("\nQuantos provedores: "))

for h in range(quantidade):
    nome = input("\nProvedor: ")
    mbps = float(input("Taxa em Mb/s (float): "))
    provedores.append(nome)
    taxaSegundo.append(mbps)

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
    if taxaSegundo[i] > max:
        max = taxaSegundo[i]
        maxIndice = i

min = maxIndice
minIndice = 0

for i in range(len(provedores)):
    print("%d| %s: %.2f mb/s" % (i+1, provedores[i], taxaSegundo[i]))
    if taxaSegundo[i] < min:
        min = taxaSegundo[i]
        minIndice = i

print("\nO provedor com pior taxa é o %s" % provedores[minIndice])
print("Provedor %s removido com sucesso\n" % provedores[minIndice])

provedores.remove(provedores[minIndice])
taxaSegundo.remove(taxaSegundo[minIndice])

for i in range(len(provedores)):
    print("%d| %s: %.2f mb/s" % (i+1, provedores[i], taxaSegundo[i]))
    if taxaSegundo[i] < min:
        min = taxaSegundo[i]
        minIndice = i

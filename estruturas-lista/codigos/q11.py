gen = [[], []]

nome = "dentro"
sexo = "d"
nman = nwon = 0

while True:
    pessoa = []
    
    nome = input("Digite \"out\" p/ sair\n\n> Nome: ")
    nome = nome.lower()
    nome = str(nome)

    if nome == "out":
        break

    pessoa.append(nome)
    sexo = input("> Sexo: ")

    if sexo[0] == "m":
        gen[0].append(pessoa)
        print("Homem inserido com sucesso!\n")

    elif sexo[0] == "f":
        gen[1].append(pessoa)
        print("Mulher inserido com sucesso!\n")
    else:
        print("Sexo inválido, encerrando operação!\n")


print("\nHomens:")
for i in range(len(gen[0])):
    print(gen[0][i])

print("\nMulheres:")
for i in range(len(gen[1])):
    print("%s" % (gen[1][i]))

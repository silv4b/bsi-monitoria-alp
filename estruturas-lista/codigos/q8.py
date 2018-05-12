nomes = []
contatos = []

numconts = 1

for i in range(numconts):
    nome = input("Nome: ")
    nomes.append(nome)
   
    contato = input("Contato: ")
    numero = str(contato)

    while len(numero) != 8:
        numero = []
        contato = input("Numero inválido\nContato: ")
        numero = str(contato)
    contatos.append(numero)

print("\nContatos:\n")
for j in range(numconts):
    print("Nome:", nomes[j])
    
    print("Contato:", end=' ')
    for e in range (len(contatos)):
        print(contatos[e])
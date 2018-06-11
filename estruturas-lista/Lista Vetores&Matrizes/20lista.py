tarefas = []
q = 1
id = 1

for i in range(q):
    t = []
    t.append(id)
    id += 1
    desc = input("Descrição: ")
    t.append(desc)
    stts = int(input("1 (Realizada)\n2 (Pendente)\nOpcao: "))
    t.append(stts)
    tarefas.append(t)

print("\nId - Descri - Status")
for i in range(len(tarefas)):
    print(tarefas[i])
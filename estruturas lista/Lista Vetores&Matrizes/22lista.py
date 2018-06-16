c = []
n = []
q = 1

for i in range(q):
    t = input("Nome: ")
    c.append(t)
    t = input("Número: ")
    while(len(t) < 8 or len(t) > 8):
        t = input("Número inválido: ")
    n.append(t)

print("\nContatos:")
for i in range(q):
    print("Nome:", c[i])
    print("Número:", n[i])
    print()

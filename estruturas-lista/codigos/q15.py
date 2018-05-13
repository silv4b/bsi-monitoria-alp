todo = []

saida = False
contador = 1

print("To-Do List")
resp = input("Adicionar pendencia (s ou n)? ")
resp = resp.lower()

while (resp[0] == 's'):
    
    pend = [0,0,0]

    pend[0] = contador
    contador += 1
    pend[1] = input("Pendência (digite-a): ")

    aux = int(input("1 p/ Pendendete\n2 p/ Completa\nStatus da pendência: "))

    if(aux == 1):
        pend[2] = "Pendente"
        todo.append(pend)
    elif(aux == 2):
        pend[2] = "Completa"
        todo.append(pend)

    resp = input("Adicionar pendencia (s ou n)? ")

print("\nPENDÊNCIAS\n")

for i in range(len(todo)):
    print("Idet.:", todo[i][0])
    print("Pend.:", todo[i][1])
    print("Stts.:", todo[i][2])
    print()
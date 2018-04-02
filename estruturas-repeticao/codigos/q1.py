aluno = input("Nome do aluno: ")
matricula = input("Matricla do aluno: ")

n1 = float(input("Nota 1: "))
while (n1 < 0) or (n1 > 10):
    if (n1 < 0) or (n1 > 10):
        print ("Nota Invalida")
        n1 = float(input("Nota 1: "))

n2 = float(input("Nota 2: "))
while (n2 < 0) or (n2 > 10):
    if (n2 < 0) or (n2 > 10):
        print ("Nota Invalida")
        n2 = float(input("Nota 2: "))

n3 = float(input("Nota 3: "))
while (n3 < 0) or (n3 > 10):
    if (n3 < 0) or (n3 > 10):
        print ("Nota Invalida")
        n3 = float(input("Nota 3: "))

print("Notas do aluno: ", aluno, "\nMatricula: ", matricula)
print("Nota 1: ", n1)
print("Nota 2: ", n2)
print("Nota 3: ", n3)
print("Media do aluno: %.2f" % ((n1+n2+n3)/3))
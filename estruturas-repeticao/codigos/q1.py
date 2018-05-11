import random

aluno = "Bruno" #aluno = input("Nome do aluno: ")
matricula = 123456789 #matricula = input("Matricla do aluno: ")

#n1 = float(input("Nota 1ª: "))
n1 = random.randint(0,10)
print(n1)
while (n1 < 0) or (n1 > 10):
    if (n1 < 0) or (n1 > 10):
        print ("\nNota Invalida")
        n1 = float(input("Nota 1ª: "))

#n2 = float(input("Nota 2ª: "))
n2 = random.randint(0,10)
print(n2)
while (n2 < 0) or (n2 > 10):
    if (n2 < 0) or (n2 > 10):
        print ("\nNota Invalida")
        n2 = float(input("Nota 2ª: "))

#n3 = float(input("Nota 3ª: "))
n3 = random.randint(0,10)
print(n3)
while (n3 < 0) or (n3 > 10):
    if (n3 < 0) or (n3 > 10):
        print ("\nNota Invalida")
        n3 = float(input("Nota 3ª: "))

print("Media do aluno: %.2f" % ((n1+n2+n3)/3))
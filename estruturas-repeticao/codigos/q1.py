# coding: utf-8

aluno = "Bruno" #aluno = input("Nome do aluno: ")
matricula = 123456789 #matricula = input("Matricla do aluno: ")

n1 = float(input("Nota 1ª: "))
while (n1 < 0) or (n1 > 10):
    if (n1 < 0) or (n1 > 10):
        print ("\nNota Invalida")
        n1 = float(input("Nota 1ª: "))

n2 = float(input("Nota 2ª: "))
while (n2 < 0) or (n2 > 10):
    if (n2 < 0) or (n2 > 10):
        print ("\nNota Invalida")
        n2 = float(input("Nota 2ª: "))

n3 = float(input("Nota 3ª: "))
while (n3 < 0) or (n3 > 10):
    if (n3 < 0) or (n3 > 10):
        print ("\nNota Invalida")
        n3 = float(input("Nota 3ª: "))

print("Media do aluno: %.2f" % ((n1+n2+n3)/3))
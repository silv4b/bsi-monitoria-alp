import random

aluno = "Bruno"  # aluno = input("Nome do aluno: ")
matricula = 123456789  # matricula = input("Matricla do aluno: ")
numeronotas = 3  # numeronotas = int(input("Número de notas: "))

contador = 0
nota = 0
notatotal = 0

while contador < numeronotas:
    #nota = float(input("Nota %dª: " % (contador+1)))
    nota = random.randint(-12, 10)
    print(nota)
    while (nota < 0 or nota > 10):
        nota = int(input("\n%dª nota está inválida, digite-a novamente: " % (contador+1)))
    notatotal = notatotal + nota
    contador += 1

print("Media do aluno: %.2f" % (notatotal/numeronotas))
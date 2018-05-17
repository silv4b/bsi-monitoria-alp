import random

aluno = "Bruno" #aluno = input("Nome do aluno: ")
matricula = 123456789 #matricula = input("Matricla do aluno: ")
numeronotas = 3 #numeronotas = int(input("Número de notas: "))

contador = nota = notatotal = 0
zero = False

while contador < numeronotas:
    nota = float(input("Nota %dª: " % (contador+1)))
    #nota = random.randint(-12, 15)
    #print(nota)
    if (nota == 0):
        zero = True
    while (nota < 0 or nota > 10):
        nota = int(input("\n%dª nota está inválida, digite-a novamente: " % (contador+1)))
    notatotal = notatotal + nota  
    print("Total (parcial):", notatotal) 
    contador += 1

media = notatotal/numeronotas

print("Media do aluno: %.2f" % media)

if (zero == True):
    situacao = "Reprovado"
#if (media <= 3 or (media < 3 and zero == True)):
elif (media <= 3):
    situacao = "Reprovado"
elif (media > 3 and media <= 6):
    situacao = "Recuperação"
elif (media >= 7 and media <= 10):
    situacao = "Aprovado"

print("Situação: ", situacao)
aluno = "Bruno" #aluno = input("Nome do aluno: ")
matricula = 123456789 #matricula = input("Matricla do aluno: ")
numeronotas = 3 #numeronotas = int(input("Número de notas: "))

contador = nota = notatotal = zero = 0

while contador < numeronotas:
    nota = float(input("Nota %dª: " % (contador+1)))
    if (nota == 0):
        zero = 1
    while (nota < 0 or nota > 10):
        nota = int(input("\n%dª nota está inválida, digite-a novamente: " % (contador+1)))
    notatotal = notatotal + nota   
    contador += 1

media = notatotal/numeronotas

print("Media do aluno: %.2f" % media)

if (media < 3 or zero == 1):
    situacao = "Reprovado"
elif (media > 3 and media < 6):
    situacao = "Recuperação"
else:
    situacao = "Aprovado"

print("Situação: ", situacao)
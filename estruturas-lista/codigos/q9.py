frase = list("o rato roeu a roupa do rei de roma")

#BEFORE
print("Frase: ", end=" ")
for j in range (len(frase)):
    print(frase[j], end=" ")

#DOING
for x in range(len(frase)):
    if (frase[x] == ' '):
        frase[x] = '-'

#AFTER
print("\nFrase: ", end=" ")
for j in range (len(frase)):
    print(frase[j], end=" ")

#R: TROCA OS ESPAÇOS POR '-'
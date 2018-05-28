p = input("\nPalavra/frase: ")
p2 = []

c = "aeiouAEIOUÁÀÃÂáàâãÉÈÊéèêÍÌÎíìîÓÒÔÕóòôõÚÙÛúùû"

for i in range(len(p)):
    if p[i] not in c:
        p2.append(p[i])

print(p2)
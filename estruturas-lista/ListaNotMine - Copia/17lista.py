p = input("\nPalavra/frase: ")

vogais = "aAeEiIoOuU"
v = c = 0

for i in range(len(p)):
    if (p[i] in vogais):
        v += 1
    else:
        c += 1

print("Nº vogais:", v)
print("Nº consoantes:", c)
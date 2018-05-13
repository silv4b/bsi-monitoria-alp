palavra = input("Palavra: ")
sumvog = 0

for i in range(len(palavra)):
    if(palavra[i] in ('a','e','i','o','u')):
        sumvog += 1

print("\nNumero de vogais:", sumvog)
print("Numero de consoantes: ", len(palavra) - sumvog)
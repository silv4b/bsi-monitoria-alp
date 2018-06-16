print("Digite 0 (zero) para finalzar")
num = int(input("Número: "))
soma = 0

while (num != 0):
    soma = soma + num
    num = int(input("Número: "))

print("Somatório: ", soma)
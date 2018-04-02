num = int(input("Digite um número: "))

while True:    
    if (num%2==0):
        print("Número %d não é primo" % num)
        num = int(input("Digite um número: "))
    else:
        break

print("Número %d é primo\nFIM!" % num)
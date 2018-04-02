#mmc

num1 = num3 = int(input("Numero 01: "))
num2 = num4 = int(input("Numero 02: "))

a = num1
b = num2

resto = None
while resto is not 0:
    resto = a % b
    a  = b
    b  = resto
    mmc = (num1 * num2) / a

print("O MMC de %d e %d é : %d" %(num3, num4, mmc))
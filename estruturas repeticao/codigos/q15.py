#mdc

num1 = num3 = int(input("Numero 01: "))
num2 = num4 = int(input("Numero 02: "))

mdc = 0
#

#resto = None
resto = 1
#while resto is not 0:
while resto != 0:
    resto = num1 % num2
    num1  = num2
    num2  = resto
    mdc = num1

print("O MDC (%d,%d) = %d" %(num3, num4, mdc))


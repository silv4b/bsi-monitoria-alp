num = int(input("Tabuada de: "))
num2 = int(input("A partir de: "))

for i in range (11-num2):
    print("%d * %d = %d" %(num, num2, (num*num2)))
    num2 = num2 + 1
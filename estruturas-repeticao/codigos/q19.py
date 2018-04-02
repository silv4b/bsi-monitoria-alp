num = int(input("Número: "))
numd = num * 2
cnum = 0

for i in range (1, num+1):
    if (num % i == 0):
        cnum = cnum + i
        print(cnum)
        

if(cnum == numd):
    print("\n%d é perfeito" % num)
else:
    print("\n%d não é perfeito" % num)

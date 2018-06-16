num = int(input("Digite um número: "))
c = 0
print("Div. p/ ", end=" ")
for n in range(1, num + 1):
    if(num%n == 0):
        print("[ %d ]" % n, end=" ")
        c += 1
    else:
        print("%d" % n, end=" ")

if(c == 2):
    print("\n%d é primo!" % num)
else:
    print("\n%d não é primo!" % num)
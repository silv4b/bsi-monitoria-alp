l = []
t = 10

for i in range(t):
    n = int(input("numero: "))
    while n == 0 or (n%2 != 0 and n >= 0):
        n = int(input("inválido -> numero: "))
    l.append(n)

print(l)
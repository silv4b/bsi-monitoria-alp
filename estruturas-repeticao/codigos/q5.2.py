n = int(input("Número: "))
t = 0

for c in range(1, n+1):
    if n % c == 0:
        print("---")
    else:
        print("===")

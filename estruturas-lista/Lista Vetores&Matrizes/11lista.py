from random import randint

d = [0]*6
r = 10

for i in range(r):
    n = randint(1,6)

    if n == 1:
        d[0] += 1
    if n == 2:
        d[1] += 1
    if n == 3:
        d[2] += 1
    if n == 4:
        d[3] += 1
    if n == 5:
        d[4] += 1
    if n == 6:
        d[5] += 1

print(" 0 "*6)
print(" 1  2  3  4  5  6 ")
print(d)
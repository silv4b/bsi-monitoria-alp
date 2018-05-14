import random

dado = [0,0,0,0,0,0]
lncs = []

for e in range(50):
    n = random.randint(1,6)
    lncs.append(n)

for i in range(len(lncs)):
    if(lncs[i] == 1):
        dado[0] += 1
    if(lncs[i] == 2):
        dado[1] += 1
    if(lncs[i] == 3):
        dado[2] += 1
    if(lncs[i] == 4):
        dado[3] += 1
    if(lncs[i] == 5):
        dado[4] += 1
    if(lncs[i] == 6):
        dado[5] += 1

print("Número 1: %d" % dado[0])   
print("Número 2: %d" % dado[1])   
print("Número 3: %d" % dado[2])   
print("Número 4: %d" % dado[3])   
print("Número 5: %d" % dado[4])   
print("Número 6: %d" % dado[5])     

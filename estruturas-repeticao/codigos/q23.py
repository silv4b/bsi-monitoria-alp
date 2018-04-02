
import time

contador = 0

inicio = time.time()

while contador < 500:
    print("contando while")
    contador += 1

fim = time.time()

tempo1 = fim - inicio

#print("\t\t",tempo1)

inicio = fim = 0

inicio = time.time()

for i in range(500):
    print("contanto for")

fim = time.time()

tempo2 = fim - inicio

#print("\t\t",tempo2)

print("\n")
print("Tempo 1", tempo1)
print("Tempo 2", tempo2)

print()

if(tempo1 > tempo2):
    print("While demorou mais")
else:
    print("For demorou mais")
from random import randint

def bubbleSort(aslist):
    n = len(aslist)
    for i in range(n):
        for j in range(n-1+(i-i)):
            if aslist[j] > aslist[j+1]:
                aux = aslist[j]
                aslist[j] = aslist[j+1]
                aslist[j+1] = aux

def makenumber(aslist, nnuns, lmitrand):
    for i in range(nnuns):
        aslist.append(randint(0-(i*20),lmitrand))

alist = []

makenumber(alist, 10, 100)
print(alist)
bubbleSort(alist)
print(alist)
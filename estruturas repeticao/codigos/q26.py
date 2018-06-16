#escreva um programa em python que receba o inicio, fim e passo
#e faça com que seja exibido do inicio ao fim, de passo em passo
#ex: inicio: 1 fim: 10 passo: 3
#1 4 7 10

inicio = int(input("inicio: "))
fim = int(input("fim: "))
passo = int(input("passo: "))

if(inicio < fim):
    for c in range(inicio, fim+1, passo):
        print(c)

while(inicio > fim):
    print("Inicio não pode ser maior que o fim")
    if(inicio > fim):
        inicio = int(input("inicio: "))
        fim = int(input("fim: "))
        passo = int(input("passo: "))
    
    for c in range(inicio, fim+1, passo):
        print(c)

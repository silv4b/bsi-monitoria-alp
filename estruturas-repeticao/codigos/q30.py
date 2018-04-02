'''
programa que exiba os n primeiros termos de uma PA (Progressão aritmética)
'''

primeiro = int(input("Primeiro termo: "))
razao  = int(input("Razão: "))

quantidade = int(input("n-ésiom termo: "))
quantidade = primeiro + (quantidade - 1) * razao

for i in range(primeiro, quantidade+1, razao):
    print("{} ".format(i), end = "-> ")
print("FIM")
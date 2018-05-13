'''m = int(input('Digite o valor de m: '))
matriz = []
n = m
for x in range(m):
	linha = []
	for y in range(m):
		if x == y:
			linha.append(1)
		else:
			linha.append(0)
	matriz.append(linha)
for i in range(m):
	for j in range (n):
		if j ==n - 1:
			print(matriz[i][j])
		else:
			print(matriz[i][j] , end =" ")'''

'''m = int(input('Digite o valor de m: '))
matriz = []
n= m
soma= 0
for x in range(m):
	linha = []
	for y in range(n):
		num = int(input('Digite o valor de n: '))
		if x == y:
			linha.append(num)
			soma+=num
		else:
			linha.append(num)
	matriz.append(linha)
for i in range(m):
	for j in range (n):
		if j ==n - 1:
			print(matriz[i][j])
		else:
			print(matriz[i][j] , end =" ")
print('Soma',soma)'''

#m = int(input('Digite o valor de m: '))
m = 3
matriz = []  # define a matriz vazia
#n = int(input('Digite o valor de m: '))
n = m
soma = 0
for x in range(m):
    linha = []  # prepara a linha vazia pra ser preenchida
    for y in range(n):  # for que preeche a linha
        #num = int(input('Digite o valor de n: '))
        num = 0
        if (num % 2 == 1):  # define se o numero é impar
            linha.append(num)
            soma += num
        else:
            linha.append(num)
    matriz.append(linha)

# EXIBIÇÃO
for i in range(m):
    print("|", end=" ")
    for j in range(n):
        print(matriz[i][j], end=" | ")
    print()
print('Soma', soma)

'''
   1   2   3
1 [ ] [ ] [ ] 1
2 [ ] [ ] [ ] 2
3 [ ] [ ] [ ] 3
   1   2   3
'''

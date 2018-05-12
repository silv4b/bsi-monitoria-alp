palavra = input("Palavra: ")

palavra_min = palavra.lower()
palavra_min = palavra_min.replace(' ', '')

print("Palavra sem espaços:", palavra_min)

palavra_invertida = palavra_min[::-1]
if palavra_min == palavra_invertida:
    print("A palavra é palíndroma.\n")
else:
    print("A palavra não é palíndroma.\n")

print('Sua palavra: ', end='')
print(palavra)

print('Inversão: ', end='')
print(palavra_invertida)

#lista com elementos a serem verificados
lista = [1,9,52,36,5,2,7,2,5,456,63]

#variavel que vau ser atualzada a cada iteralçao, caso a condição satisfaça
maior = 0

#laço que percorre a lista (len(lista)) -> tamanho (int) da lista
for i in range(len(lista)):
    #condição de verificação do elemento da lista
    if lista[i] > maior:
        #condição satisfeita e variavel atualizada
        maior = lista[i]

'''
sempre que o if for ssatisfeito e o elemento da lista for maior que o elemento atual da variavel maior,
a mesma sera atualzada, essa verificação ocorre durante da iteração do for.
'''

print("Maior elemento: ", maior)
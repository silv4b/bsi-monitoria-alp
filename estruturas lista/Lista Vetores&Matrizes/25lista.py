plv = palindromo = pse = []

p = input("\nPalavra/frase: ")
p = p.lower() #não desenrolei a implementação do lower().

for i in range(len(p)):
    plv.append(p[i])

a = "âáàã"
e = "éèê"
i = "ìíî"
o = "òóôõ"
u = "úùû"
cc = "ç"
pts = "\"',!¹-_+=/*@#$%¨& "

#Verifica caracteres especiais
for g in range(len(p)):
    if plv[g] in a:
        plv[g] = 'a'
    if plv[g] in e:
        plv[g] = 'e'    
    if plv[g] in i:
        plv[g] = 'i'
    if plv[g] in o:
        plv[g] = 'o'
    if plv[g] in u:
        plv[g] = 'u'
    if plv[g] in cc:
        plv[g] = 'c'

#Verifica os espaços e os "ignoram"
for h in range(len(p)):
    if plv[h] in pts:
        pse.append(plv[h])

#Prenche uma lista de tras pra frente (palavra invertida)
cont = len(pse)-1
while cont >= 0:
    palindromo.append(pse[cont])
    cont -= 1

#comparação
if pse == palindromo:
    print("\nÉ palindroma")
else:
    print("\nNão é palindroma")
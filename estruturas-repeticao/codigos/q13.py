salario = float(input("Salário: "))
percentual = float(input("Percentual: "))
anoi = int(input("Ano inicial: "))
anof = int(input("Ano final: "))
while (anoi <= anof):
    print ("Ano: %i Percentual: %.1f%% Salario: R$ %.2f" % (anoi, percentual, salario))
    salario += (salario * percentual)
    percentual *= 2
    anoi += 1

print ("Salario atual do funcionario: R$ %.2f" % (salario))
salario = 500.0
percentual = 0.15
ano = 2010

while (ano <= 2018):
    salario = salario + (salario * percentual)
    print ("Ano: %i Percentual: %.2f%% Salario: R$ %.2f" % (ano, percentual, salario))
    percentual *= 2
    ano += 1

print ("Salario atual do funcionario: R$ %.2f" % (salario))
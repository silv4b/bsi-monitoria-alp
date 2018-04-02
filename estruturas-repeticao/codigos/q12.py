salario = 988.00
percentual = 1.5
ano = 2010

while (ano <= 2018):
    print ("Ano: %i Percentual: %.1f%% Salario: R$ %.2f" % (ano, percentual, salario))
    salario += (salario * (percentual / 100.0))
    percentual *= 2
    ano += 1

print ("Salario atual do funcionario: R$ %.2f" % (salario))

'''
programa que aceite apenas o sexo M ou F como entrada e n permita outras opções
'''

sexo = input("Sexo: ")
sexo = sexo.upper()

while True:
    if (sexo == 'M' or sexo == 'F'):
        print("Sexo válido!")
        break
    else:
        print("opção inválida.")
        sexo = input("Sexo: ")
        sexo = sexo.upper()
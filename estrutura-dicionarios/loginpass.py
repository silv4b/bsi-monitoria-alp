import functions as func

users = {}

func.limpatela()

users ["admin"] = "admin"
users ["isk4"] = "8569574"
users ["jeanegathinha"] = "asd3213a"
users ["sasuke"] = "naruto"
users ["j0n4asss"] = "asd123"

print()
print('='*23)
print('='*3, "Logins e Senhas", '='*3)
print('='*23)

for (k,v) in users.items():
    #não exibe admin
    if(k == "admin"):
        continue

    print("\n > User :", v)
    #print(" > Senha:", k)
    print(" > Senha:", '*'*len(k))

print()
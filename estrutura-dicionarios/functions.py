import os
from datetime import datetime

def limpatela():
    os.system('cls' if os.name == 'nt' else 'clear')

def questao(n):
    print('='*23)
    print('='*6,"Questão {}".format(n).strip(),'='*6)
    print('='*23)

def timedate():
    now = datetime.now()
    day = now.day
    month = now.month
    year = now.year
    minutes = now.minute
    hour = now.hour
    print("Dia",day,"do",month,"de", year,"")
    print(hour,"Hrs e",minutes,"Min")
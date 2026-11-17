import time
from calculadora2 import *

#teste = soma_dois_numeros(20,30)
#print(teste)

#teste2 = divide_dois_numeros
#print(teste2)

numero1 = float(input("Primeiro número: "))
time.sleep(5)
numero2 = float(input("Segundo número: "))

teste3 = multiplica_dois_numeros(numero1,numero2)
teste4 = divide_dois_numeros(numero1,numero2)
print(teste3,teste4)
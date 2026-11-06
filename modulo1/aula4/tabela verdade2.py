'''
Para me deslocar até o senac nova iguaçu, preciso pegar:
- trem
- onibus
- metro
'''

tren = input("Voce veio de trem? ")
input("Voce veio de onibus? ")
input("Voce veio de metro? ")

if trem == "sim" or onibus == "sim" or metro == "sim":
    print("Bem-vindo(a) ao senac!")
else:
    print("tarifa dinamica")  
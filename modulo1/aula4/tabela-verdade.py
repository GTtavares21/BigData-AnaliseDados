
### contexto 1: (uso do operador AND)

'''
para queeu possa dirigir, eu preciso ter:
-documento (CNH) em posse;
- maioridade (+18); 
- não estar acloolizado.
'''

pergunta1 = input("voce tem os documentos em mãos? ")
pergunta2 = int(input("qual a sua idade? "))
pergunta3 = input("voce consumiu bebida alcolica antes de dirigir? ")

if pergunta1 == "sim" and pergunta2 >= 18:
    print("pode dirigir.")
elif pergunta1 == "sim" and pergunta3 == "sim":
    print("não pode dirigir.")


 ###Contexto2:    

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

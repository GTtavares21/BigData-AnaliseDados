
### contexto 1:

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
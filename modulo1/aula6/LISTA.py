##Listas
# índices    0         1        2        3       4
compras = ["arroz", "feijao", "sabão", "pão", "açucar"]


compras2 = [
    "amaciante", "papel toalha", "farinha", "maçã", "pão de forma"]

compras_final = compras + compras2
#print(compras_final)

compras3 = [
    "laranja",
    "maçã",
    "hamburguer",
    "sal"
]

compras_final += compras3
#print(compras_final)

#compras_final += ["café"]
#compras_final.append("café")
compras_final.insert(2,"café")
#print(compras_final)
compras_final.pop(4)
compras_final.remove("maçã")
compras_final.pop()
compras_dezembro=compras_final.copy()
#print(compras_dezembro)

compras_final.count("maçã")
compras_final.clear()

#print(compras_final)
#print(compras_dezembro)

##TUPLAS:

tupla_compras = tuple(compras_dezembro)
#print(compras_final)

tupla_compras =("leite")
#print(tupla_compras)




#filmes_final_semana = {
    #"O menino e A Garça", 
    #"As Branquelas", 
    #"Premonição",
    #"Premonição", 
    #"Avenger", 
    #"Diarios de uma Paixão"
#

#for i in filmes_final_semana:
 #   print(i)

##Dicionarios

filmes = {
    "Titanic": [1996, "Drama/Romance", 10], 
    "Como Treinar Seu Dragão": 2010,
    "Shrek": 2001,
    "Star Wars IV": 1984
    }

#print(filmes["Titanic"][1])

nomes_filmes = ["Titanic", "Shrek"]
ano_lancamento_filme = [1997, 2001]
genero_filme = ["Drama/Romance", "Comedia/Animação"]
indicadores_oscar = ["Sim", "Sim"]

titanic_info = ["Titanic", 1997, "Drama/Romance", "Sim"]


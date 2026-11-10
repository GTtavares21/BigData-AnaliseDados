## USO DO MATCH CASE

#ANTES: IF/ELSE

print("############## ATENDIMENTO OUTHERE ################")

categorias = ["Massas", "Bebidas", "Petiscos", "Doces", "Salgados", "Pizzas", "Churrasco", "Lanches", "Comida Japonesa", "Pastel"]
print(categorias)

pergunta = input("Escolha uma das categorias acima:")

if pergunta == "Massas":
    print("Dia das Massas, com rodizio e descontos é toda na quarta-feira!")
elif pergunta == "Massas":
     print("Dia das Bebidas, com rodizio e descontos é toda na quarta-feira!")
elif pergunta == "Bebidas":
     print("Dia das Petiscos, com rodizio e descontos é toda na quarta-feira!")
elif pergunta == "Petiscos":
     print("Dia das Doces, com rodizio e descontos é toda na quarta-feira!")
elif pergunta == "Doces":
     print("Dia das Salgados, com rodizio e descontos é toda na quarta-feira!")
elif pergunta == "Salgados":
     print("Dia das Pizzas, com rodizio e descontos é toda na quarta-feira!")
elif pergunta == "Pizzas":
     print("Dia das Massas, com rodizio e descontos é toda na quarta-feira!")
elif pergunta == "Churrasco":
     print("Dia das Churrasco, com rodizio e descontos é toda na quarta-feira!")
elif pergunta == "Lanches":
     print("Dia das Lanches, com rodizio e descontos é toda na quarta-feira!")
elif pergunta == "Comida Japonesa":
     print("Dia das Comida Japonesa, com rodizio e descontos é toda na quarta-feira!")
elif pergunta == "Pastel":
     print("Dia das Pastel, com rodizio e descontos é toda na quarta-feira!")
else:
     print("Opção invalida. por favor tente novamente.")
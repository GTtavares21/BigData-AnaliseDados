codigo = int(input("Digite o código de origem do produto: "))

if codigo == 1:
    print("Região de procedencia : Sul")
elif codigo == 2:
    print("Região de procedencia : Norte")
elif codigo == 3:
    print("Região de procedencia : Leste")
elif codigo == 4:
    print("Região de procedencia : Oeste")
elif codigo == 5 or codigo == 6:
    print("Região de procedencia : Nordeste")
elif codigo == 7 or codigo == 8 or codigo == 9:
    print("Região de procedencia : Sudeste")
elif codigo == 10:
    print("Região de procedencia : Centro-Oeste")
elif codigo == 11:
    print("Região de procedencia : Noroeste")
else:
    #caso não seja nenhum dos codigos acima, é considerado importado.
    print("Região de procedencia : Importado")

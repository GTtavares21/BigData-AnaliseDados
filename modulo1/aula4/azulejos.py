#Dimensões da cozinha
comprimento = float(input("Digite o comprimento da cozinha(m): "))
largura = float(input("Digite a largura da cozinha(m): "))
altura = float(input("Digite a altura da cozinha(m): "))

#calculando a area das 4 paredes
area_paredes = (2 * comprimento * altura) + (2 * largura * altura)

#calculando quantas caixas
caixas = area_paredes / 1.5

print(f"Área total: {area_paredes} m")
print(f"caixas necessarias {caixas}")

if caixas <= 5:
    print("categoria: cozinha pequena")
elif caixas <= 15:
    print("categoria: cozinha media")
else:
    print("categoria: cozinha grande")
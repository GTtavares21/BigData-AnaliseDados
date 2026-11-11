#dimensões 
largura = float(input("Digite a largura da sala(metros): "))
comprimento = float(input("Digite o comprimento da sala(metros): "))
#calculo
area = largura * comprimento 

quantidade_lampadas = area / 3

print(f"Área do comodo: {area}m²")

if area <= 3:
    print("Quantidade exata de lampada necessária: 1")
elif area <= 6:
    print("Quantidade exata de lampada necessária: 2")
elif area <= 9:
    print("Quantidade exata de lampada necessária: 3")
elif area <= 12:
    print("Quantidade exata de lampada necessária: 4")
else:
    print(f"Quantidade exata de lâmpadas necessárias: {int(quantidade_lampadas) + 1}")
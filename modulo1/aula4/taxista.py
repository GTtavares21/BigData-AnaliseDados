
preco_combustivel = 6.15

odometro_inicio = float(input("Digite a marcação do odometro no inicio do dia (km): "))
odometro_fim = float(input("Digite a marcação do odometro no fim do dia (km): "))
litros_gasto = float(input("Digite o númrto de litros de combustivel gasto: "))
valor_recebido = float(input("Digite o valor total recebido dos passageiros (R$): "))

km_rodados = odometro_fim - odometro_inicio

if litros_gasto > 0:
    media_consumo = km_rodados / litros_gasto
else:
    media_consumo = 0

custo_combustivel = litros_gasto * preco_combustivel
lucro_liquido = valor_recebido - custo_combustivel

print("\n--- Resultados ---")
print(f"Quilometros rodados: {km_rodados:.2f} km")
print(f"Media de consumo: {media_consumo:.2f} km/L")
print(f"Custo com combustivel: R$ {custo_combustivel:.2f}")
print(f"Lucro liquido do dia: R$ {lucro_liquido:.2f}")

if lucro_liquido > 200:
    print("Avaliação: ótimo dia de trabalho!")
elif lucro_liquido > 100:
    print("Avaliação: bom dia de trabalho.")
else:
    print("Avaliação: dia fraco de ganhos.")
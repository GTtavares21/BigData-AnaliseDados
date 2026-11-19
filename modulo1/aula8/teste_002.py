##DIFERENÇAS ENTRE COPY E ARMAZENAMENTO-PADRÃO:

insetos = [
    "mosca", "louva-deus", "barata", "lacraia"
]

insetos2 = insetos
insetos3 = insetos.copy()

insetos.clear()

print(insetos)
print(insetos2)
print(insetos3)
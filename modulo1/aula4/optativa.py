
nota1 = float(input("digite a primeira nota: "))
nota2 = float(input("digite a segunda nota: "))
notaO = float(input("digite a nota optativa: "))


media = (nota1 + nota2 + notaO)

print("Notas:", nota1, nota2, notaO)


if  media > 6:
    print("Status: Aprovado!")
elif  3 <= media:
    print("Status: Reprovado.")
else:
    print("Status: Recuperação.")
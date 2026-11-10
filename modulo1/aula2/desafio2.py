
nota1 = float(input("digite a primeira nota: "))
nota2 = float(input("digite a segunda nota: "))
nota3 = float(input("digite a terceira nota: "))
nota4 = float(input("digite a quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

print("Notas:", nota1, nota2, nota3, nota4)


if  media > 7:
    print("Status: Aprovado!")
elif  5 <= media <= 7:
    print("Status: Recuperação.")
else:
    print("Status: Reprovado.")
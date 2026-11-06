#variaveis:
nmr1 = float(input("Informe seu primeiro número: "))
nmr2 = float(input("Informe seu segundo número: "))
#operações:
soma = nmr1+nmr2
subtracao = nmr1 - nmr2
multiplicacao = nmr1 * nmr2

print("Res soma:", soma) 
print("Res multiplicacao:", multiplicacao)
print("Res subtracao:", subtracao)

if nmr2 != 0:
    divisao = nmr1 / nmr2
    print("Res divisao:", divisao)
else:
    print("Res divisao: Não é possível dividir por zero!")    
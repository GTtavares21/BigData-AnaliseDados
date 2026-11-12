##CADASTRO DE CANDIDATOS

for i in range(1,13):
    print(f"---Candidato {i}---")

    ano_nascimento = int(input("Digite a seu ano de nascimento: "))
    idade = 2026 - ano_nascimento
    #Caso for menor de idade.
    if idade < 18:
        print("Acesso negado! Idade não corresponde.")
        print("Pulando para o próximo usuario...")
    #Caso for maior de idade.
    else:    
        print("Prossiga com cadastro.")
        telefone = float(input("Digite o número de telefone: "))
        email = (input("Digite o seu email: "))
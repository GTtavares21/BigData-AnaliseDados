## Funções

#
def menu_inicial():
    print("*"*40)
    print("#### ATENDIMENTO LAITI ####")
    print("*"*40)
    print("Para iniciarmos seu atendimento, por favor digite o cpf")
    nome_user = input("Nome: ")
    id_user = input("CPF: ")
    print(f"Olá, {nome_user}! Seu identificador informado é {id_user}.")

menu_inicial()
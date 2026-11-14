##LOGIN

#usuario e senha corretos:

usuario_correto = "admin"
senha_correta = "senha500"

#numero de tentativas permitidas.
tentativas = 3
while tentativas > 0:
    print(f"Tentativas restantes {tentativas}")

    usuario_digitado = input("Digite nome de usuario: ")
    senha_digitada = input("Digite a senha: ")

    #verificar se login esta correto.
    if usuario_digitado == usuario_correto and senha_digitada == senha_correta:
        print("Sucesso! login efetuado com exito.")
        break
    else:
        print("Usuario ou senha incorretos.")
        tentativas -= 1 

        
if tentativas == 0:
    print("\nAcesso bloqueado! Suas tentativas acabaram.")
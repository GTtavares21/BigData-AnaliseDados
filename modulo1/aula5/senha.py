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
email = "fred@gmail.com"
senha = "fred123"

while True:
    n_email = str(input("Digite seu e-mail: "))
    n_senha = str(input("Digite sua senha: "))
    if n_email == email and n_senha == senha:
        print("Acesso liberado!")
        break
    else:
        print("e-mail ou senha incorretos.")
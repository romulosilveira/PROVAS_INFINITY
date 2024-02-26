senha = "abc"
sen = 0

for tentativas in range(3):
    sen = str(input("Digite a senha: ")) 
    if sen == senha:
        print("Bem vindo.")
        break
    if tentativas == 0 and sen != senha:
        print(f"Senha errada. Você ainda possui duas tentativas.")
    if tentativas == 1 and sen != senha:
        print(f"Senha errada. Você ainda possui uma tentativa.")
    if tentativas == 2 and sen != senha:
        print(f"Senha errada. Você não possui mais tentativas. Acesso bloqueado.")
num = 0
contador_num = 0
soma = 0
media = 0

while True:
    num = int(input("Digite um número inteiro ['0' para finalizar]: "))
    if num > 0:
        contador_num += 1
        soma = soma + num
        media = soma/contador_num
    elif num < 0:
        print("Digite um número positivo.")
    else:
        num == 0
        print(f"Quantidade de números digitados: {contador_num}")
        print(f"Soma dos números digitados: {soma}")
        print(f"Média dos números digitados: {media}")
        break
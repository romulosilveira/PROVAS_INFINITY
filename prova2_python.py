lista = []

for x in range(10):
    num = int(input("Digite um valor: "))
    lista.append(num)

numeros_pares = []
numeros_impares = []

for num in lista:
    if num % 2 == 0:
        numeros_pares.append(num)
    else:
        numeros_impares.append(num)

print(f"Números pares: {numeros_impares}.")
print(f"Números ímpares: {tuple(numeros_impares)}.")
print(f"Quantidade de números pares: {len(numeros_pares)}.")
print(f"Quantidade de números ímpares: {len(numeros_impares)}.")
print(f"A soma dos números da lista é: {sum(lista)}.")
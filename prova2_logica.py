velocidade = int(input("Digite a velocidade do automóvel em km/h: "))
pot_multa = 0
multa = 0

if velocidade > 80:
    pot_multa = velocidade - 80
    multa = pot_multa * 20
    print(f"Você foi multado no valor de {multa} reais por exceder a velocidade máxima permitida.")
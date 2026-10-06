velocidade = float(input("Digite a velocidade do carro em km/h: "))

if velocidade > 80:
    excesso = velocidade - 80
    multa = excesso * 5

    print("Você foi multado!")
    print(f"Velocidade acima do limite: {excesso:.2f} km/h")
    print(f"Valor da multa: R$ {multa:.2f}")
else:
    print("Você está dentro do limite de velocidade.")

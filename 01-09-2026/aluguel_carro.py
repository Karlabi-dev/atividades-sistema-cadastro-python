km = float(input("Digite a quantidade de km percorridos: "))
dias = int(input("Digite a quantidade de dias de aluguel: "))

valor_diarias = dias * 60
valor_km = km * 0.15
total = valor_diarias + valor_km

print(f"Valor das diárias: R$ {valor_diarias:.2f}")
print(f"Valor dos quilômetros: R$ {valor_km:.2f}")
print(f"Preço total a pagar: R$ {total:.2f}")

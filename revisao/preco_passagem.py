distancia = float(input("Digite a distância da viagem em km: "))

if distancia <= 200:
    preco_km = 0.50
else:
    preco_km = 0.45

preco_passagem = distancia * preco_km

print(f"Preço da passagem: R$ {preco_passagem:.2f}")

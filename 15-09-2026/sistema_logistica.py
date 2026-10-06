rota = ["Sao Paulo", "Campinas", "Jundiai", "Sorocaba"]
novas_cidades = ["Itu", "Valinhos"]

rota.extend(novas_cidades)
posicao = rota.index("Sorocaba")

print("Rota completa:", rota)
print(f"Posição de Sorocaba: {posicao}")
print(f"Sorocaba é a {posicao + 1}ª cidade da rota")

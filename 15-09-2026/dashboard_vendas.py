vendas = [1500, 2000, 800, 3500, 1200]

total = sum(vendas)
media = total / len(vendas)
melhor_venda = max(vendas)
pior_venda = min(vendas)

print("===== RELATÓRIO DE VENDAS =====")
print(f"Total de vendas: R$ {total:.2f}")
print(f"Média de vendas diária: R$ {media:.2f}")
print(f"Melhor venda: R$ {melhor_venda:.2f}")
print(f"Pior venda: R$ {pior_venda:.2f}")

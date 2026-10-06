preco = float(input("Digite o preço da mercadoria: R$ "))
percentual = float(input("Digite o percentual de desconto: "))

desconto = preco * percentual / 100
preco_pagar = preco - desconto

print(f"Valor do desconto: R$ {desconto:.2f}")
print(f"Preço a pagar: R$ {preco_pagar:.2f}")

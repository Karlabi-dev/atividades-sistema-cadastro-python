preco = float(input("Digite o preço da mercadoria: R$ "))
porcentagem = float(input("Digite a porcentagem de desconto: "))

desconto = preco * porcentagem / 100
preco_final = preco - desconto

print(f"Valor do desconto: R$ {desconto:.2f}")
print(f"Preço a pagar: R$ {preco_final:.2f}")

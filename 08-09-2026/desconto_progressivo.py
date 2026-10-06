import re

entrada = input("Digite o valor total da compra: R$ ")

entrada = re.sub(r'R\$\s*', '', entrada, flags=re.IGNORECASE)
entrada = entrada.strip()
entrada = entrada.replace('.', '').replace(',', '.')

valor = float(entrada)

if valor >= 500:
    percentual = 15
elif valor >= 200:
    percentual = 10
else:
    percentual = 0

desconto = valor * percentual / 100
valor_final = valor - desconto

print(f"Valor da compra: R$ {valor:.2f}")
print(f"Valor do desconto: R$ {desconto:.2f}")
print(f"Valor final a pagar: R$ {valor_final:.2f}")

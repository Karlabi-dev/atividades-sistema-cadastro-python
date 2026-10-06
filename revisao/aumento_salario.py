salario = float(input("Digite o salário do funcionário: R$ "))

if salario > 1250:
    percentual = 10
else:
    percentual = 15

aumento = salario * percentual / 100
novo_salario = salario + aumento

print(f"Valor do aumento: R$ {aumento:.2f}")
print(f"Novo salário: R$ {novo_salario:.2f}")

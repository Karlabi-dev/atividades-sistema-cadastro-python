salario = float(input("Digite o valor do salário: R$ "))
porcentagem = float(input("Digite a porcentagem de aumento: "))

aumento = salario * porcentagem / 100
novo_salario = salario + aumento

print(f"Valor do aumento: R$ {aumento:.2f}")
print(f"Novo salário: R$ {novo_salario:.2f}")

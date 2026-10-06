import re

entrada = input("Digite o valor que deseja investir: R$ ")

entrada = re.sub(r'R\$\s*', '', entrada, flags=re.IGNORECASE)
entrada = entrada.strip()
entrada = entrada.replace('.', '').replace(',', '.')

valor = float(entrada)

if valor < 1000:
    print("Perfil iniciante: Sugerimos Tesouro Direto")
elif valor <= 5000:
    print("Perfil moderado: Sugerimos Fundos Imobiliários")
else:
    print("Perfil arrojado: Sugerimos Ações")

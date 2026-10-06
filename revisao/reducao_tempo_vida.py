cigarros_dia = int(input("Digite a quantidade de cigarros fumados por dia: "))
anos = int(input("Digite há quantos anos você fuma: "))

minutos_perdidos = cigarros_dia * 10
dias_fumando = anos * 365
total_minutos = minutos_perdidos * dias_fumando
total_dias = total_minutos / 1440

print(f"Total de dias de vida perdidos: {total_dias:.2f} dias")

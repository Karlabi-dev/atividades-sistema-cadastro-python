precos = [100.0, 250.0, 500.0]
vinhos = ["Branco", "Tinto", "Champagne"]

nome = input("Digite o nome do produto: ")
novo_preco = float(input("Digite o novo preço: R$ "))

if nome in vinhos:
    posicao = vinhos.index(nome)
    precos[posicao] = novo_preco

    print("\nProduto atualizado com sucesso!")
    print("\n===== LISTA DE PRODUTOS =====")

    for i in range(len(vinhos)):
        print(f"{vinhos[i]} - R$ {precos[i]:.2f}")
else:
    print("Produto não encontrado.")

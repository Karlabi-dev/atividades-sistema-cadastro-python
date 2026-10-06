estoque = ["monitor", "teclado", "mouse", "headset"]

estoque.append("webcam")
estoque[1] = "teclado mecanico"

print("Impressora está no estoque?", "impressora" in estoque)

estoque.remove("mouse")

print("Estoque final:", estoque)

balas = int(input("Quantas balas no pacote: "))
pessoas = int(input("Quantidade de pessoas: "))


recebera = balas // pessoas
resto1 = balas % pessoas


print(f"Quantidade de balas por pessoa {recebera:.0f} ")
print(f"Sobrarão: {resto1:.0f} ")


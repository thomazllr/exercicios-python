plastico = int(input("Quantidade de clips de plástico: "))
metal = int(input("Quantidade de clips de metal: "))

valor_metal = metal * 10
valor_plastico = plastico * 5
valor_total = valor_metal + valor_plastico

print(f"Valor arrecadado por caixas de plástico: {valor_plastico}")
print(f"Valor arrecadado por caixas de metal: {valor_metal}")
print(f"Valor arrecadado total: {valor_total}")
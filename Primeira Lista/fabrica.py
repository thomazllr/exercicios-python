//Uma fábrica produz dois tipos de clips, plástico ou metal, sendo que a caixa de cada tipo
é vendida por 5 e 10 reais, respectivamente. Faça um algoritmo em que o usuário forneça
a quantidade de caixas vendidas de clips de plástico e de metal e informe qual será o
valor arrecadado com cada um dos tipos e o valor total arrecadado.//

plastico = int(input("Quantidade de clips de plástico: "))
metal = int(input("Quantidade de clips de metal: "))

valor_metal = metal * 10
valor_plastico = plastico * 5
valor_total = valor_metal + valor_plastico

print(f"Valor arrecadado por caixas de plástico: {valor_plastico}")
print(f"Valor arrecadado por caixas de metal: {valor_metal}")
print(f"Valor arrecadado total: {valor_total}")
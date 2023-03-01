distancia = int(input("Digite a distância percorrida do carro: "))
valor_combustivel = float(input("Digite o valor do combustível: "))
consumo_medio = float(input("Digite o consumo médio: "))

gasolina_consumida = distancia / consumo_medio

valor_total = gasolina_consumida * consumo_medio

print(f"Gasolina consumida: {gasolina_consumida}")
print(f"Valor total: R$ {valor_total}")

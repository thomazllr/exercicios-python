n1 = float(input("Digite a quatidade de água consumida em m³: "))
tipo = input("Digite o tipo de consumo: ")

if tipo == "Residencial":
    valor = 5.00 + (n1 * 0.05)
    print(f"Valor total da conta de água: R$ {valor}")

if tipo == "Comercial":
    if n1 <= 80:
        valor = 500.00
        print(f"Valor total da conta de água: R$ {valor}")
    elif n1 > 80:
        valor = 500.00 + (0.25 * (n1-80))
        print(f"Valor total da conta de água: R$ {valor}")


if tipo == "Industrial":
    if n1 >= 100:
        valor = 800
        print(f"Valor total da conta de água: R$ {valor}")
    elif n1 > 100:
        valor = 800.00 + (0.04 * (n1-100))
        print(f"Valor total da conta de água: R$ {valor}")

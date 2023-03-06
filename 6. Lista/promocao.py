n1 = float(input("Digite a quantidade de combustível: "))
comando = input("Digite o comando a seguir\n"
                "==================================\n"
                "G para Gasolina\n"
                "A para Álcool: ")
print("==================================")

if comando == "G":
    if n1 <= 30 and n1 >= 20:
        total = (n1 * 7.00) - ((n1 * 7.00) * 0.05)
        print(f"O valor da gasolina com aplicação de desconto de 5%: R$ {total}")
    elif n1 > 30:
        total = (n1 * 7.00) - ((n1 * 7.00) * 0.10)
        print(f"O valor da gasolina com aplicação de desconto de 10%: R$ {total}")
    else:
        total = (n1 * 7.00)
        print(f"O valor da gasolina ficou: R$ {total}")


if comando == "A":
    if n1 <= 30 and n1 >= 20:
        total = (n1 * 5.00) - ((n1 * 5.00) * 0.05)
        print(f"O valor da gasolina com aplicação de desconto de 5%: R$ {total}")
    elif n1 > 30:
        total = (n1 * 5.00) - ((n1 * 5.00) * 0.10)
        print(f"O valor da gasolina com aplicação de desconto de 10%: R$ {total}")
    else:
        total = (n1 * 7.00)
        print(f"O valor da gasolina ficou: R$ {total}")
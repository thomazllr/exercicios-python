n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
print("==================================")
comando = input("Digite o comando a seguir\n"
                "==================================\n"
                "c para crescente\n"
                "d para decrescente: ")

if comando == "c":
    if n1 > n2:
        print(f"Ordem crescente: {n2}, {n1}")
    else:
        print(f"Ordem crescente: {n1}, {n2}")
if comando == "d":
    if n1 > n2:
        print(f"Ordem decrescente: {n1}, {n2}")
    else:
        print(f"Ordem decrescente: {n2}, {n1}")

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
n3 = int(input("Digite outro número: "))

if n1 != 0 and n2 != 0 and n3 != 0:
    print("Todos os números são diferentes de zero")
    if n1 > 0 and n2 > 0 and n3 > 0:
        produto = n1 * n2 * n3
        print(f"O produto dos números é: {produto}")
    elif n1 > 0 or n2 > 0 or n3 > 0:
        soma = n1 + n2 + n3
        print(f"A soma dos números é {soma}")
    elif n1 < 0 and n2 < 0 and n3 < 0:
        media = (n1 + n2 + n3) / 3
        print(f"A média dos números é {media}")
elif n1 == 0 and n2 == 0 and n3 == 0:
    print("Todos os números são iguais a zero")

else:
    print("Nem todos os números são diferentes de zero")
    if (n1 == 0 and n2 == 0) or (n1 == 0 and n3 == 0) or (n2 == 0 and n3 == 0):
        print("Dois números iguais a zero")
    else:
        print("Um número igual a zero")


         

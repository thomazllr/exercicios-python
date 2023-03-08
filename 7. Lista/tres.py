n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
n3 = int(input("Digite outro número: "))

if n1 != 0 and n2 != 0 and n3 != 0:
    print("Todos os números são diferentes de zero")

else:
    print("Nem todos os números são diferentes de zero")
    if n1 != 0 or n2 != 0:
        print("Um número é igual a zero")
    else:
        print("Dois números é igual a zero")


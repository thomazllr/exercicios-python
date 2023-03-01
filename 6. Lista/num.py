num = float(input("Informe um número: "))

if num > 0:
    print("Número positivo")
    num = num * 2
    print(num)
elif num < 0:
    print("Número negativo")
    if num % 2 == 0:
        print("Número par")
    else:
        print("Número ímpar")
else:
    print("Número igual a zero")
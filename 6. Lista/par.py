n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

soma = n1 + n2

if soma % 2 == 0:
    soma = soma / 2
    print(soma)
else:
    print("ímpar")
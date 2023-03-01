n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

if n2 == 0:
    print("Não pode ser feita divisão por zero!")
else:
    divisao = n1 / n2
    print(f"Resultado da divisão: {divisao:.0f}")
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

if n1 > n2:
    diferenca = n1 - n2
    print(f"A diferença do maior pro menor é {diferenca}")
elif n1 < n2:
    diferenca = n2 - n1
    print(f"A diferença do maior pro menor é {diferenca}")
else:
    soma = n1 + n2
    print(f"A soma dos números iguais é {soma}")

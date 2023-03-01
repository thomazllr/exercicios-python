n1 = float(input("Digite o primeiro lado: "))
n2 = float(input("Digite o segundo lado: "))

if n1 == n2:
    print("É um quadrado perfeito")
elif n1 > n2:
    print(f"Lado maior é o L1: {n1}")
else:
    print(f"Lador menor é o L2: {n2}")
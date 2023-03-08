n1 = int(input("Digite um número: "))

if n1 >= 10 and n1 <= 50:
    print("Está no intervalo")
else:
    if n1 < 10:
        print("Vem antes")
    else:
        print("Vem depois")
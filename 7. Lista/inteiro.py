n1 = int(input("Digite o primeiro número: "))

if n1 % 2 == 0 and n1 > 0:
    metade = n1  // 2
    print(f"A metade do número é {metade}")
else:
    dobro = n1 * 2
    print(f"O dobro do número é {dobro}")
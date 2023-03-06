sala1 = int(input("Digite a quantidade de alunos na primeira sala: "))
sala2 = int(input("Digite a quantidade de alunos na primeira sala: "))
sala3 = int(input("Digite a quantidade de alunos na primeira sala: "))

total = sala1 + sala2 + sala3
qt_leite = total // 4
custo = qt_leite * 3.5

if total % 4 == 0:
    print(f"Total de crianças: {total}")
    print(f"Quantidade de litros de leite: {qt_leite:.0f}")
    print(f"Custo: R$ {custo}")
else:
    qt_leite = total // 4 + 1
    custo = qt_leite * 3.5
    print(f"Total de crianças: {total}")
    print(f"Quantidade de litros de leite: {qt_leite}")
    print(f"Custo: R$ {custo:.1f}")

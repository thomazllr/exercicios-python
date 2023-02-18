//Escreva um algoritmo que leia três números inteiros e positivos (A, B, C) e calcule a seguinte expressão://

A = int(input("Digite o primeiro número: "))
B = int(input("Digite o segundo número: "))
C = int(input("Digite o terceiro número: "))

R = (A + B) * (A + B)
S = (C + B) * (C + B)

D = (R + S) / 2

print(f"Resultado da expressão: {D:.0f}")
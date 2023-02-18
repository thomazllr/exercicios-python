//Antes do racionamento de energia ser decretado, quase ninguém falava em quilowatts,
mas agora, todos a incorporaram a seu vocabulário. Sabendo que cada quilowatt de
energia custa um centésimo do salário mínimo, escreva um algoritmo que receba o valor
do salário mínimo e a quantidade de quilowatts gasta em uma residência, calcule e
imprima o valor pago pela residência em questão.//

salario = int(input("Digite o seu salário: "))
watts = int(input("Digite a quantidade de watts: "))

valor_pago = watts * (salario * 0.01)

print(f"Valor pago pela residência: {valor_pago}")

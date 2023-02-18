//João recebeu seu salário e precisa pagar duas contas que estão atrasadas. Como as contas estão
atrasadas, João terá de pagar multa de 2% sobre cada conta. Faça um programa que leia o valor do
salário, o valor de cada uma das contas, calcule e mostre o valor que João pagou em cada conta e
quanto restarádo salário do João.//

salario = float(input("Digite o salário de João: "))
conta1 = float(input("Digite o valor da primeira conta: "))
conta2 = float(input("Digite o valor da segunda conta: "))

multa1 = conta1 + (conta1 * 0.02)
multa2 = conta2 + (conta2 * 0.02)
multa_final = conta1 + conta2 + multa1 + multa2
restante_salario = salario - multa_final

print(f"Conta 1 = R$ {multa1:.2f}")
print(f"Conta 2 = R$ {multa2:.2f}")
print(f"Restante do salário =  {restante_salario:.0f}")

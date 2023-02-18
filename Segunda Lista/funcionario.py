//Escreva um programa que leia o número de um funcionário, seu número de horas trabalhadas em um
mês e o valor que ele recebeu por hora. Imprima o número e o salário que o funcionário receberá no
final do mês//

n1 = int(input("Número do funcionário: "))
horas = int(input("Quantidade de horas trabalhadas: "))
valor = float(input("Valor recebido por hora: "))

salario = horas * valor

print(f"Número =  {n1:.0f}")
print(f"Salário = R$ {salario:.2f}")
n1 = int(input("Número do funcionário: "))
horas = int(input("Quantidade de horas trabalhadas: "))
valor = float(input("Valor recebido por hora: "))

salario = horas * valor

print(f"Número =  {n1:.0f}")
print(f"Salário = R$ {salario:.2f}")
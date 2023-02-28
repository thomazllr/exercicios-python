valor_hora = float(input("Digite o valor da hora: "))
qtd_hora = float(input("Quantidade de hora trabalhada: "))     
pct_desconto = float(input("Digite o percentual de desconto com impostos: "))

salario_bruto = valor_hora * qtd_hora
desconto = salario_bruto - (salario_bruto * (pct_desconto/100))

salario_liquido = salario_bruto - desconto

print(f"Salário Bruto: {salario_bruto}\n"
      f"Valor do desconto: {desconto}\n"
      f"Salário Líquido: {salario_liquido}\n")

n1 = int(input("Digite o salário bruto: "))
n2 = int(input("Valor previsto: "))

if n2 < (n1 * 0.30):
    print("Empréstimo concedido")
else:
    print("Empréstimo não concedido")

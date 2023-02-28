anos = int(input("Digite a idade em anos: "))
meses = int(input("Digite os meses: "))
dias = int(input("Digite os dias: "))



dias_totais = (anos * 365) + (meses * 30) + dias

print(f"Dias totais: {dias_totais}")
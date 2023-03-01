homens = int(input("Digite a quantidade de homens: "))
mulheres = int(input("Digite a quantidade de mulheres: "))

total = homens + mulheres

pct_mulher = (mulheres * 100) / total
pct_homem = (homens * 100) / total

print(f"Total de alunos: {pct_homem} %")
print(f"Porcentagem de mulheres {pct_mulher} %")
print(f"Porcentagem de homens {pct_homem} %")
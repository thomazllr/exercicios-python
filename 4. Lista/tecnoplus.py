nome = input("Digite seu nome: ")
email = input("Digite seu email: ")
print(f"Parabéns {nome}! Seu cadastro foi realizado com sucesso e vc ganhou um cumpom de 10% para a sua primeira compra")

valor = int(input("Valor total da compra: "))

desconto = valor * 0.10
valor_final = valor - desconto

print(f"O valor total da sua compra é R$ {valor}. Com cupom de desconto, vc terá um desconto de {desconto} e o valor final será de {valor_final}")
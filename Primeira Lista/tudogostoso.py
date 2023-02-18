//O restaurante “Tudo Gostoso” cobra R$ 30.00 pelo quilo de refeição. Escreva um
programa que lê o peso do prato cheio de um cliente (em quilos) e imprima o valor a
pagar.
* Considere que o peso do prato é 0.8 Kg.//

kg = float(input("Digite a quantidade de kilogramas do seu prato: "))

pagar = (kg + 0.8) * 30

print(f"A sua conta no restauprante deu R$ {pagar}")
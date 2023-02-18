//Faça um programa que leia o nome e duas notas de um aluno, calcule e apresente seu
nome e a sua média aritmética, no seguinte modelo:
Fulano obteve a média XX.//

nome = input("Digite seu nome: ")
n1 = int(input("Digite a primeira nota: "))
n2 = int(input("Digite a segunda nota: "))

media = (n1+n2) / 2

print(f"A média do aluno {nome} é {media}")
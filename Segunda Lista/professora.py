//Uma professora precisa calcular a média de um aluno. O aluno realizou 3 provas, sendo que a
primeira prova tem peso 1, a segunda tem peso 2 e a terceira prova tem peso 3. Escreva um
programa que leia o nome do aluno e as notas, calcule e apresente a média ponderada do aluno.
//

n1 = int(input("Digite a primeira nota: "))
n2 = int(input("Digite a segunda nota: "))
n3 = int(input("Digite a terceira nota: "))

media = (n1 + (n2 * 2) + (n3 * 3)) / 6


print(f"Resultado da média do aluno: {media:.2f}")
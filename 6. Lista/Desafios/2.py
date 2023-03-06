ano1 = int(input("Digite o ano que a primeira pessoa nasceu: "))
mes1 = int(input("Digite o mês que a primeira pessoa nasceu: "))
dia1 = int(input("Digite o dia que a primeira pessoa nasceu: "))
print("======================================================")
ano2 = int(input("Digite o ano que a segunda pessoa nasceu: "))
mes2 = int(input("Digite o mês que a segunda pessoa nasceu: "))
dia2 = int(input("Digite o dia que a segunda pessoa nasceu: "))

idade1 = 365 * ano1 + mes1 * 30 + dia1
idade2 = 365 * ano2 + mes2 * 30 + dia2

if idade1 < idade2:
    print("A primeira pessoa é mais velha")
elif idade1 > idade2:
    print("A segunda pessoa é mais velha")
else:
    print("Possuem idade igual")

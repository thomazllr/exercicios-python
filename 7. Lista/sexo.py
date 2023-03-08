sexo = input("Qual o sexo? ")
turno = input("Digite o turno do aluno: ") 

if sexo == "M" and turno == "M":
    print("Bom dia, querido!")
elif sexo == "M" and turno =="V":
    print("Boa tarde, querido!")
elif sexo == "F" and turno == "M":
    print("Bom dia, querida!")
else:
    print("Boa tarde, querida!")
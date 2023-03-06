tipo1 = input("======== Digite o tipo do animal ======== \n"
"Vertebrado ou Invertebrado: ")
print("==========================")
tipo2 = input("======== Digite o tipo do animal ======== \n"
"Para Vertebrado - Ave ou Mamifero: \n"
"Para Invertebrado - Inseto ou Anelideo: ")
print("==========================")

tipo3 = input("======== Digite o tipo do animal - (Alimentação) ======== \n"
"Carnivoro // Herbivaro // Onivoro // Hematofago: ")

if tipo1 == "Vertebrado":
    if tipo2 == "Ave" and tipo3 == "Carnivoro":
        print("Águia")
    elif tipo2 == "Ave" and tipo3 == "Onivoro":
        print("Pomba")
    elif tipo2 == "Mamifero" and tipo3 == "Onivoro":
        print("Homem")
    elif tipo2 == "Mamifero" and tipo3 == "Herbivoro":
        print("Vaca")

if tipo1 == "Invertebrado":
    if tipo2 == "Inseto" and tipo3 == "Hematofago":
        print("Pulga")
    elif tipo2 == "Inseto" and tipo3 == "Herbivoro":
        print("Lagarta")
    elif tipo2 == "Anelideo" and tipo3 == "Hematofago":
        print("Sanguessuga")
    elif tipo2 == "Anelideo" and tipo3 == "Onivoro":
        print("Minhoca")

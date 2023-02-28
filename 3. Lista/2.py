segundos = int(input("⌚ - Segundos: "))

hora = segundos // 3600
resto1 = segundos % 3600

minutos = resto1 // 60
segundos = resto1 % 60

print(f"{hora} hora(s) - {minutos} minuto(s) - {segundos} segundo(s)")


amount = float(input("¿cuanto quieres inevertir? "))
interest = float(input("¿interes anual? "))
years = int(input("¿Años?"))
print("Capital final: " + str(round(amount * (interest / 100 + 1) ** years, 2)))
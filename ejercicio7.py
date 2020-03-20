horas = float(input("Introduce tus horas de trabajo: "))
coste = float(input("cuanto cobra por hora: "))
paga = round(horas * coste, 3)
print("entonces te van a pagar " + str(paga))
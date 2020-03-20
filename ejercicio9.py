weight = input("¿cuanto pesas? ")
height = input("¿estatura en metros?")
bmi = round(float(weight)/float(height)**2,2)
print("Tu índice de masa corporal es " + str(bmi))
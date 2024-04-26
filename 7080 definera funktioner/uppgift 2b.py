def farenhight_to_celsius (farenhight):
    celsius = (5/9) * (farenhight - 32)
    return celsius
F = float (input("Ange temperaturen i Farenhight: "))
print ("Temperaturen är", farenhight_to_celsius(F), "C")
def celsius_to_farenhight (celsius):
    F = (9/5) * celsius + 32
    return F
celsius = float (input("Ange temperatur i celsius: "))
print ("Temperaturen är", celsius_to_farenhight(celsius), "F")



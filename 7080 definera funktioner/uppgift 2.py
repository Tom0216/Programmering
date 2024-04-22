"""
def celsius_to_farenhight (celsius):
    F = (9/5) * celsius + 32
    return F
celsius = float (input("Ange temperatur i celsius: "))
print ("Temperaturen är", celsius_to_farenhight(celsius), "F")
"""
def farenhight_to_celsius (farenhight):
    celsius = (5/9) * (farenhight - 32)
    return celsius
F = float (input("Ange temperaturen i Farenhight: "))
print ("Temperaturen är", farenhight_to_celsius(F), "C")

def kelvin_to_farenhight (kelvin):
    f = 9.0/5 * (kelvin - 273.15) +32
    return f
kelvin = float (input("Ange temperatur i kelvin:"))
print ("Temperaturen är",kelvin_to_farenhight(kelvin), "F")
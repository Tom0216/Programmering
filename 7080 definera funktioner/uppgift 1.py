def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

#Omvanling = float (input("Omvanldar Kelvin till Celsius:"))
print (" ") 

kelvin = float(input("Ange temperatur i Kelvin: "))
print("Temperaturen är", kelvin_to_celsius(kelvin), "Celsius")


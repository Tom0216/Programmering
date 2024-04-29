def celsius_to_farenhight (celsius):
    F = (9/5) * celsius + 32
    return F

def farenhight_to_celsius (farenhight):
    celsius = (5/9) * (farenhight - 32)
    return celsius

def kelvin_to_celsius (kelvin):
    return kelvin - 273.15

def kelvin_to_farenhight (kelvin):
    f = 9.0/5 * (kelvin - 273.15) +32
    return f

def celsius_to_kelvin(celsius):
    kelvin = 273.15 + celsius
    return kelvin

def farenhight_to_kelvin(farenheight):
    celsius = farenhight_to_celsius(farenheight)
    kelvin = celsius_to_kelvin(celsius)
    return kelvin

def läs_input():
    print("Omvandla från:")
    print("1. kelvin → celsius")
    print ("2. kelvin → farenhight")
    print ("3. celsius → farenhight")
    print ("4. celsius → kelvin")
    print ("5. farenhight → celsius")
    print ("6.farenhight → kelvin")
    print("7. för att avsluta.")
    svar = input("välj: ")
    return svar

svar = läs_input()


while svar !="7":
    if svar == "1":
        kelvin = float (input("Ange temperatur i kelvin → Celsius:"))
        print ("Temperaturen är", kelvin_to_celsius(kelvin), "celsius")
    if svar == "2":
        kelvin = float (input("Ange temperatur i kelvin → Farenhight:"))
        print ("Temperaturen är",kelvin_to_farenhight(kelvin), "farenhight")
    if svar == "3":
        celsius = float (input("Ange temperatur i Celsius → Farenhight:"))
        print ("Temperaturen är",celsius_to_farenhight(celsius), "farenhight" )
    if svar == "4":
        celsius = float (input("Ange temperatur i Celsius → Kelvin:"))
        print ("Temperaturen är", celsius_to_kelvin(celsius), "kelvin")
    if svar == "5":
        farenhight = float (input("Ange temperatur i farenhight → Celsius:"))
        print ("Temperaturen är", farenhight_to_celsius(farenhight), "celsius")
    if svar == "6":
        farenhight = float (input("Ange temperatur i farenheight → Kelvin:"))
        print ("Temperaturen är", farenhight_to_kelvin(farenhight), "kelvin")

    svar = läs_input()
print ("Tack för att du spelade :)")

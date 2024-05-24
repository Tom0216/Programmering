def hästkrafter_to_kilowatt (hästkrafter):
    kilowatt = 0.746 * hästkrafter 
    return kilowatt

def kilowatt_to_hästkrafter (kilowatt):
    hästkrafter = kilowatt / 0.746
    return hästkrafter

def kilometerpertimme_to_meterpersekund (kilometerpertimme):
     meterpersekund = kilometerpertimme /3.6
     return meterpersekund

def meterpersekund_to_kilometerpertimme (meterpersekund):
     kilometerpertimme = meterpersekund *3.6
     return kilometerpertimme

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

def kvadratmeter_to_hektar(kvadratmeter):
     # 1000 000 = 10 000 * 100
     # 1000 000 / 10 000 = 100
     hektar = kvadratmeter /10000
     return hektar

def hektar_to_kvadratmeter (hektar):
     kvadratmeter = hektar *10000
     return kvadratmeter

def kvadratmeter_to_tunnland (kvadratmeter):
     tunnland = kvadratmeter / 4046.85
     return tunnland

def tunnland_to_hektar (tunnland):
     hektar = tunnland * 0.4936
     return hektar

def hektar_to_tunnland (hektar):
     tunnland = hektar /0.4936
     return tunnland

def tunnland_to_kvadratmeter (tunnland):
     kvadratmeter = tunnland * 4046.85
     return kvadratmeter
     

def läs_input():
    print ("Vad vill du omvandla?")
    print ("1. Effekt (hästkraft, kilowatt)")
    print ("2. Hastighet (km/h, m/s)")
    print ("3. Temperatur (celsius, farenheight, kelvin)")
    print ("4. Areaenheter (kvadratmeter, hektar, tunnland)")
    print ("5. Recept: Mått (deciliter, kryddmått, matsked, tesked)")
    print ("6. Recept: Volym, vikt för olika livsmedel (mjöl, makaroner, socker)")
    svar = input("välj:")
    return svar

def  läs_input_hästkraft_kilowatt():
    print ("Vad vill du omvandla?")
    print("1. hästkrafter → kilowatt")
    print("2. kilowatt → hästkrafter")
    svar = input("välj:")
    return svar

def läs_input_kilometerpertimme_to_meterpersekund():
     print ("Vad vill du omvandla?")
     print ("1. km/h → m/s")
     print ("2. m/s → km/h")
     svar = input("välj:")
     return svar

def läs_input_celsius_to_farenhight():
    print ("Vad vill du omvandla?")
    print("1. kelvin → celsius")
    print ("2. kelvin → farenhight")
    print ("3. celsius → farenhight")
    print ("4. celsius → kelvin")
    print ("5. farenhight → celsius")
    print ("6.farenhight → kelvin")
    svar = input("välj: ")
    return svar

def läs_input_kvadratmeter_to_hektar():
     print ("Vad vill du omvandla?")
     print ("1. kvadratmeter → hektar")
     print ("2. Hektar → Kvadratmeter")
     print ("3. Kvadratmeter → tunnland")
     print ("4. Tunnland → hektar")
     print ("5. Hektar → tunnland")
     print ("6. Tunnland → Kvadratmeter")
     svar = input("välj: ")
     return svar

def test():
    # test ok
    hektar = kvadratmeter_to_hektar(99)
    kvadratmeter = hektar_to_kvadratmeter(hektar)
    print("rätt svar 99, faktiskt svar: ", kvadratmeter)



svar = läs_input()



while svar == "1":

    svar = läs_input_hästkraft_kilowatt()

    if svar == "1":
            hästkrafter = float (input("Ange effekten i Hästkraften → Kilowatt:"))
            print ("Effekten är", hästkrafter_to_kilowatt(hästkrafter), "kilowatt")

    if svar == "2":
            kilowatt = float (input("Ange effekten i Kilowatt → Hästkraft:"))
            print ("Efftekten är", kilowatt_to_hästkrafter(kilowatt), "hästkrafter")

while svar == "2":
    svar = läs_input_kilometerpertimme_to_meterpersekund()

    if svar == "1":
            kilometerpertimme = float (input("Ange hastigheten i km/h → m/s:"))
            print ("Hastigheten är",kilometerpertimme_to_meterpersekund(kilometerpertimme), "m/s") 
    
    if svar == "2":
            meterpersekund = float (input("Ange hastigheten i m/s → km/h:"))
            print ("Hastigheten är", meterpersekund_to_kilometerpertimme (meterpersekund), "km/h")

while svar == "3":
    svar = läs_input_celsius_to_farenhight()

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

while svar == "4":
    svar = läs_input_kvadratmeter_to_hektar()

    if svar == "1":
          kvadratmeter = float (input("Ange längden i kvadratmeter → hektar: "))
          print ("Längden blir",kvadratmeter_to_hektar(kvadratmeter), "hektar")
    
    if svar =="2":
         hektar = float (input("Ange längden i hektar → kvadratmeter:"))
         print ("Längden blir",hektar_to_kvadratmeter(hektar), "kvadratmeter")
    
    if svar == "3":
         kvadratmeter = float (input("Ange längden i kvadratmeter → tunnland:"))
         print ("Längden blir", kvadratmeter_to_tunnland(kvadratmeter), "tunnland")

    if svar == "4":
         tunnland = float (input("Ange längden i tunnland → hektar: "))
         print ("Längden blir",tunnland_to_hektar(tunnland), "hektar")

    if svar == "5":
         hektar = float (input("Ange längden i hektar → tunnland:"))
         print ("Längden blir",hektar_to_tunnland (hektar), "tunnland")

    if svar == "6":
         tunnland = float (input("Ange längden i tunnland → kvadratmeter:"))
         print ("Längden blir", tunnland_to_kvadratmeter (tunnland), "kvadratmeter")

        
    svar = läs_input()
print ("Tack för att du spelade :)")
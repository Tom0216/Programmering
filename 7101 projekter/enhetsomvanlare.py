#1. Effekt
def hästkrafter_to_kilowatt (hästkrafter):
    kilowatt = 0.746 * hästkrafter 
    return kilowatt

def kilowatt_to_hästkrafter (kilowatt):
    hästkrafter = kilowatt / 0.746
    return hästkrafter

#2. Tryck
def pascal_to_bar (pascal):
     bar = pascal /100000
     return bar

def pascal_to_atmosfär (pascal):
     atmosfär = pascal /101325
     return atmosfär

def pascal_to_torr (pascal):
     torr = pascal /133.322
     return torr

def pascal_to_psi (pascal):
     psi = pascal * 145.04/1000000
     return psi

def bar_to_pascal (bar):
     pascal = bar * 1 * 0.00001
     return pascal

def bar_to_atmosfär (bar):
     atmosfär = bar /1.01325
     return atmosfär

def bar_to_torr (bar):
     torr = bar * 1.3332/1000
     return torr

def bar_to_psi (bar):
     psi = bar * 68.948/1000
     return psi

def atmosfär_to_pascal (atmosfär):
     pascal = atmosfär * 9.8692/1000000
     return pascal

def atmosfär_to_bar (atmosfär):
     bar = atmosfär *0.98692
     return bar

def atmosfär_to_torr (atmosfär):
     torr = atmosfär * 1.3158/1000
     return torr

def atmosfär_to_psi (atmosfär):
     psi = atmosfär /( 68.046/1000)
     return psi

def psi_to_pascal (psi):
     pascal = psi *6.894*1000
     return pascal

def psi_to_Bar (psi):
     bar = psi *14.5037744
     return bar

def psi_to_atmosfär (psi):
     atmosfär = psi * 14.696
     return atmosfär

def psi_to_torr (psi):
     torr = psi/ (19.337*10000)
     return torr

def torr_to_pascal (torr):
     pascal = torr /(7.5006/1000)
     return pascal

def torr_to_bar (torr):
     bar = torr * 750.06
     return bar

def torr_to_atmosfär (torr):
     atmosfär = torr * 760
     return atmosfär

def torr_to_psi (torr):
     psi = torr * 51.715
     return psi

#3. Hastighet
def kilometerpertimme_to_meterpersekund (kilometerpertimme):
     meterpersekund = kilometerpertimme /3.6
     return meterpersekund

def meterpersekund_to_kilometerpertimme (meterpersekund):
     kilometerpertimme = meterpersekund *3.6
     return kilometerpertimme
#4. Temperatur
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
#5. Areaenheter
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
# 6. Recept mått
def kryddmått_to_deciliter (kryddmått):
     deciliter = kryddmått * 0.01
     return deciliter

def deciliter_to_kryddmått (deciliter):
     kryddmått = deciliter * 100
     return kryddmått

def deciliter_to_matsked (deciliter):
     matsked = deciliter * 100.0 / 15
     return matsked

def deciliter_to_tesked (deciliter):
     tesked = deciliter * 20
     return tesked

def kryddmått_to_tesked (kryddmått):
     tesked = kryddmått /5
     return tesked

def kryddmått_to_matsked (kryddmått):
     matsked = kryddmått /15
     return matsked

def tesked_to_deciliter (tesked):
     deciliter = tesked /20
     return deciliter

def tesked_to_matsked (tesked):
     matsked = tesked /3
     return matsked

def tesked_to_kryddmått (tesked):
     kryddmått = tesked *5
     return kryddmått

def matsked_to_kryddmått (matsked):
     kryddmått = matsked *15
     return kryddmått

def matsked_to_deciliter (matsked):
     deciliter = matsked * 0,15
     return deciliter

def matsked_to_tesked (matsked):
     tesked = matsked * 3
     return tesked

def läs_input():
    print ("Vad vill du omvandla?")
    print ("1. Effekt (hästkraft, kilowatt)")
    print ("2. Tryck (pascal, bar, atmosfär, torr, (psi)skålpunds kraft per kvadratum)")
    print ("3. Hastighet (km/h, m/s)")
    print ("4. Temperatur (celsius, farenheight, kelvin)")
    print ("5. Areaenheter (kvadratmeter, hektar, tunnland)")
    print ("6. Recept: Mått (deciliter, kryddmått, matsked, tesked)")
    print ("7. Vill du avsluta")
    svar = input("välj:")
    return svar

def  läs_input_hästkraft_kilowatt():
    print ("Vad vill du omvandla?")
    print("1. hästkrafter → kilowatt")
    print("2. kilowatt → hästkrafter")
    svar = input("välj:")
    return svar

def läs_input_pascal_to_bar():
     print ("Vad vill du omvandla?")
     print ("1. Pascal → Bar")
     print ("2. Pascal → Atmosfär")
     print ("3. Pascal → Torr")
     print ("4. Pascal → Psi ")
     print ("5. Bar → Pascal")
     print ("6. Bar → Atmosfär")
     print ("7. Bar → Torr")
     print ("8. Bar → psi")
     print ("9. Atmosfär → Pascal")
     print ("10. Atmosfär → Bar")
     print ("11. Atmosfär → Torr")
     print ("12. Atmosfär → psi")
     print ("13. psi → Pascal")
     print ("14. psi → Bar")
     print ("15. psi → Atmosfär")
     print ("16. psi → Torr")
     print ("17. Torr → Pascal")
     print ("18. Torr → Bar")
     print ("19. Torr → Atmosfär")
     print ("20. Torr → psi")
     svar = input("Välj:")
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


def läs_input_kryddmått_to_deciliter():
     print ("Vad vill du omvandla?")
     print ("1. Kryddmått → deciliter")
     print ("2. Deciliter → kryddmått")
     print ("3. Deciliter → Matsked")
     print ("4. Deciliter → Tesked")
     print ("5. kryddmått → Tesked")
     print ("6. Kryddmått → Matsked")
     print ("7. Tesked → Deciliter")
     print ("8. Tesked → Matsked")
     print ("9. Tesked → Kryddmått")
     print ("10. Matsked → Kryddmått ")
     print ("11. Matsked → Deciliter")
     print ("12. Matsked → Tesked ")
     svar = input("välj: ")
     return svar



svar = läs_input()



while svar == "1":

    svar = läs_input_hästkraft_kilowatt()

    if svar == "1":
            hästkrafter = float (input("Ange effekten i Hästkraften → Kilowatt:"))
            print ("Effekten är", hästkrafter_to_kilowatt(hästkrafter), "kilowatt")

    if svar == "2":
            kilowatt = float (input("Ange effekten i Kilowatt → Hästkraft:"))
            print ("Effekten är", kilowatt_to_hästkrafter(kilowatt), "hästkrafter")

while svar == "2":

     svar = läs_input_pascal_to_bar()

     if svar == "1":
          pascal = float (input("Ange trycket i Pascal → Bar:"))
          print ("Trycket blir", pascal_to_bar (pascal), "Bar")

     if svar == "2":
          pascal = float (input("Ange trycket i Pascal → Atmosfär:"))
          print ("Trycket blir", pascal_to_atmosfär (pascal), "Bar")

     if svar == "3":
          pascal = float (input("Ange trycket i Pascal → Torr:"))
          print ("Trycket blir", pascal_to_torr (pascal), "Torr")

     if svar == "4":
          pascal = float (input("Ange trycket i Pascal → psi:"))
          print ("Trycket blir", pascal_to_psi (pascal), "psi")

     if svar == "5":
          bar = float (input("Ange trycket i Bar → Pascal:"))
          print ("Trycket blir", bar_to_pascal (bar), "Pascal")

     if svar == "6":
          bar = float (input("Ange trycket Bar → Atmosfär:"))
          print ("Trycket blir", bar_to_atmosfär (bar), "Atmosfär")
     
     if svar == "7":
          bar = float (input("Ange trycket i Bar → Torr:"))
          print ("Trycket blir", bar_to_torr (bar), "Torr")

     if svar == "8":
          bar = float (input("Ange trycket i Bar → psi:"))
          print ("Trycket blir", bar_to_psi (bar), "psi")
     
     if svar == "9":
          atmosfär = float (input("Ange trycket i Atmosfär → Pascal:"))
          print ("Trycket blir", atmosfär_to_pascal (atmosfär), "Pascal")

     if svar == "10":
          atmosfär = float (input("Ange trycket i Atmosfär → Bar:"))
          print ("Trycket blir", atmosfär_to_bar (atmosfär), "Bar")

     if svar == "11":
          atmosfär = float (input("Ange trycket i Atmosfär → Torr:"))
          print ("Trycket blir", atmosfär_to_torr (atmosfär), "Torr")

     if svar == "12":
          atmosfär = float (input("Ange trycket i Atmosfär → psi:"))
          print ("Trycket blir", atmosfär_to_psi (atmosfär), "psi")

     if svar == "13":
          psi = float (input("Ange trycket i psi → Pascal:"))
          print ("Trycket blir", psi_to_pascal (psi), "Pascal")

     if svar == "14":
          psi = float (input("Ange trycket i psi → Bar:"))
          print ("Trycket blir", psi_to_Bar (psi), "Bar")

     if svar == "15":
          psi = float (input("Ange trycket i psi → Atmosfär:"))
          print ("Trcket blir", psi_to_atmosfär (psi), "Atmosfär")

     if svar == "16":
          psi = float (input("Ange trycket i psi → Torr:"))
          print ("Trycket blir", psi_to_torr (psi), "Torr")

     if svar == "17":
          torr = float ("Ange trycket i Torr → Pascal:")
          print ("Trycket blir", torr_to_pascal (torr), "Pascal")

     if svar == "18":
          torr = float ("Ange trycket i Torr → Bar:")
          print ("Trycket blir", torr_to_bar (torr), "Bar")

     if svar == "19":
          torr = float ("Ange trycket i Torr → Atmosfär:")
          print ("Trycket blir", torr_to_atmosfär (torr), "Atmosfär")

     if svar == "20":
          torr = float ("Ange trycket i Torr → psi:")
          print ("Trycket blir", torr_to_psi (torr), "psi")

while svar == "3":
    svar = läs_input_kilometerpertimme_to_meterpersekund()

    if svar == "1":
            kilometerpertimme = float (input("Ange hastigheten i km/h → m/s:"))
            print ("Hastigheten är",kilometerpertimme_to_meterpersekund(kilometerpertimme), "m/s") 
    
    if svar == "2":
            meterpersekund = float (input("Ange hastigheten i m/s → km/h:"))
            print ("Hastigheten är", meterpersekund_to_kilometerpertimme (meterpersekund), "km/h")

while svar == "4":
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

while svar == "5":
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

while svar == "6":
    svar = läs_input_kryddmått_to_deciliter()

    if svar == "1":
         kryddmått = float (input("Ange mängden i Kryddmått → Deciliter:"))
         print ("Mängden blir",kryddmått_to_deciliter (kryddmått), "deciliter" )

    if svar == "2":
         deciliter = float (input("Ange mängden i Deciliter → Kryddmått:"))
         print ("Mängden blir", deciliter_to_kryddmått (deciliter), "kryddmått")

    if svar == "3":
         deciliter = float (input("Ange mängden i Deciliter → Matsked:"))
         print ("Mängden blir", deciliter_to_matsked (deciliter), "Matsked")
    
    if svar == "4":
         deciliter = float (input("Ange mängden i Deciliter → Tesked:"))
         print ("Mängden blir", deciliter_to_tesked (deciliter), "Tesked")

    if svar == "5":
         kryddmått = float (input("Ange mängden kryddmått → Tesked:"))
         print ("Mängden blir", kryddmått_to_tesked (kryddmått), "Tesked") 

    if svar == "6":
         kryddmått = float (input("Ange mängden i Krydmått → Matsked:"))
         print ("Mängden blir", kryddmått_to_matsked (kryddmått), "Matskedar")
    svar = läs_input()

    if svar == "7":
         tesked = float (input("Ange mängden i Tesked → Deciliter:"))
         print ("Mängden blir", tesked_to_deciliter (tesked), "Deciliter")

    if svar =="8":
         tesked = float (input("Ange mängden i Tesked → Matsked:"))
         print ("Mängden blir", tesked_to_matsked (tesked), "Matskedar")
     
    if svar == "9":
         tesked = float (input("Ange mängden i Tesked → Kryddmått:"))
         print ("Mängden blir", tesked_to_kryddmått (tesked), "Kryddmått")
         
    if svar == "10":
         matsked = float (input("Ange mängden i Matsked → Kryddmått:"))
         print ("Mängden blir", matsked_to_kryddmått (matsked), "Kryddmått")

    if svar == "11":
         matsked = float (input("Ange mängden i Matsked → Deciliter:"))
         print ("Mängden blir", matsked_to_deciliter (matsked), "Deciliter")

    if svar == "12":
         matsked = float (input("Ange mängden i Matsked → Tesked:"))
         print ("Mängden blir", matsked_to_tesked (matsked), "Tesked")

if svar == "7":
     print("Tack för att du spelade :)")
     print ("SLUT")

def hästkrafter_to_kilowatt (hästkrafter):
    kilowatt = 0.746 * hästkrafter 
    return kilowatt

def kilowatt_to_hästkrafter (kilowatt):
    hästkrafter = kilowatt / 0.746
    return hästkrafter

def km/h_to_m/s 

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
    print("1. hästkrafter → kilowatt")
    print("2. kilowatt → hästkrafter")
    svar = input("välj:")
    return svar

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

        
    svar = läs_input()
print ("Tack för att du spelade :)")
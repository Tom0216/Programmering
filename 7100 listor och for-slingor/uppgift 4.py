text=input("Ange ett ord")

svar = ""
Bokstäver = "abcdefghijklmnopqrstuvwxyz"
svar = ""




for bokstav in text:
    tal = ord(bokstav)    
    print(tal, bokstav)
    tal = tal + 2
    if tal > ord("z"):
        tal = tal - 26
    ny_bokstav = chr(tal)
    svar = svar + ny_bokstav

print (svar)


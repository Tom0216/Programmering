text=input("Ange ett ord")
svar = ""
Bokstäver = "abcdefghijklmnopqrstuvwxyz"
svar = ""



for bokstav in text:
    tal = ord(bokstav)
    tal = tal - 2
    ny_bokstav = chr(tal)
    svar = svar + ny_bokstav

print (svar)


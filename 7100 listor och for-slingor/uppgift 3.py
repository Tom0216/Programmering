vokal =  ["A", "O", "U", "Å", "E", "I", "Y", "Ä", "Ö"]
konsonant = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Z"]
#konsonant= konsonant + "O" + konsonant
text=input("Ange ett ord")
#ord = int(text)
#print (ord)

svar = ""

# för varje bokstav i ord
for bokstav in text:
    if bokstav in konsonant:
        svar = svar + bokstav + "o" + bokstav        
    else:
        if bokstav in vokal:
            svar = svar + bokstav
print (svar)

# om bokstav är konsonant
# lägg till bokstaven + o + bokstaven
# i svar
# annars
# lägg till bokstaven i svar

# skriv ut svar

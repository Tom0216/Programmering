kod= "en haerlig vinter"

svar = ""
Bokstäver = "abcdefghijklmnopqrstuvwxyz"
chiffer=    "zyxwvutsrqponmlkjihgfedcba"


svar = ""
for bokstav in kod:
    # index för bokstav i Bokstäver
    i = Bokstäver.find(bokstav)
    # lägg till bokstaven på index från chiffer i svar
    svar = svar + chiffer[i]

    
print (svar)
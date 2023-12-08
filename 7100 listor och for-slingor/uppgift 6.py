kod= "lwthni_lnqqfw_qtb_bjnlmy_utqdstrnfq_rzqynuqjx"

svar = ""
Bokstäver = "abcdefghijklmnopqrstuvwxyz"
chiffer= "zyxwvutsrqonmlkjihgfedcba"
svar = ""

for bokstav in kod:
    tal = ord(bokstav)    
    print(tal, bokstav)
    tal = tal + 10
    if tal > ord("z"):
        tal = tal - 26
    ny_bokstav = chr(tal)
    svar = svar + ny_bokstav
print (svar)
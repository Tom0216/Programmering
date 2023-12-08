kod= "lwthni_lnqqfw_qtb_bjnlmy_utqdstrnfq_rzqynuqjx"

svar = ""
Bokstäver = "abcdefghijklmnopqrstuvwxyz"
chiffer= "zyxwvutsrqonmlkjihgfedcba"

for index in range(1,27):
    svar = ""
    for bokstav in kod:
        if bokstav == "_":
            svar = svar + bokstav
        else:
            tal = ord(bokstav)    
            #print(tal, bokstav)
            tal = tal + index
            if tal > ord("z"):
                tal = tal - 26
            ny_bokstav = chr(tal)
            svar = svar + ny_bokstav
    print (svar)
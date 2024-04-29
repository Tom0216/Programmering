# ta två tal 
# beräkna summan
# returnera summan
def summa (tal_ett, tal_två):
    svar = tal_ett + tal_två
    return svar
print ("Beräkna summan av två heltal")
text = input("Tal 1: ")
tal_1 = int(text)
text = input("Tal 2: ")
tal_2 = int(text)

print ("svar")
print ("Talen blir", summa(tal_1, tal_2), "sammanlagt")
# testa funktionen
# ge den två tal 
# skriv ut svaret
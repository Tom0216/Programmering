print("Du har 5 gissningar")
svar =int(input("Gissa på rätt tal"))
antal_gissningar = 1
while svar !=42 and antal_gissningar < 5:
    if svar > 42:
        svar = int(input("för mycket"))
    elif svar <42:
        svar = int(input("för litet"))
    antal_gissningar = antal_gissningar +1
if svar == 42:
    print ("Rätt")
print(antal_gissningar)
print("klar")

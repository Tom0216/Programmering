print("Du har 5 gissningar")
svar = input("Vad heter Norges huvudstad")
antal_gissningar = 1
while svar !="Oslo" and antal_gissningar < 3:
    if svar =="Oslo":
        svar = int(input("Rätt"))
    elif svar != "Oslo":
        svar = input("Pröva igen")
    antal_gissningar = antal_gissningar +1
if svar == "Oslo":
    print ("Rätt")
print (antal_gissningar)
print("Klar")
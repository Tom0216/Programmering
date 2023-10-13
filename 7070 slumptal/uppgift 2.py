import random
fråga = input ("Skriv (j) för att spela och (n) för att sluta")
while fråga=="j":
    t1 = random.randrange(1,10)
    t2 = random.randrange(1,10)
    t3 = random.randrange(1,10)
    print (t1, t2, t3)
    if t1== 7 and t2== 7 and t3== 7:
        print ("dubbel vinst")
    elif t1==t2==t3:
        print ("vinst")
    else:
        print ("förlust")
    fråga =input ("Skriv (j) för att spela och (n) för att sluta")
print ("Tack för att du spelade, välkommen åter!")
print ("klar")
import random
print ("start 100 kr")
print ("varje spel = -1 kr")
print ("vinst = 50 kr")
print ("dubbelvinst = 100 kr")
print ("minivinst = 5 kr")
print("sjuvinsten = 2 kr")
pengar = 100
print ("Kvar att spela för:,", pengar, "kronor")
fråga = input ("Skriv (j) för att spela och (n) för att sluta")
while fråga=="j":
    t1 = random.randrange(1,10)
    t2 = random.randrange(1,10)
    t3 = random.randrange(1,10)
    print (t1, t2, t3)
    pengar= pengar -1
    if t1== 7 and t2== 7 and t3== 7:
        print ("dubbel vinst + 100 kr")
        pengar= pengar + 100
        print ("kvar att spela för", pengar)
    elif t1==t2 or t2==t3 or t3==t1:
        print("minivinst + 5 kr")
        pengar = pengar + 5
        print ( "Kvar att spela för", pengar)
    if t1==7 or t2==7 or t3==7:
        print("sjuvinst + 2 kr")
        pengar= pengar +2
        print ("Kvar att spela för", pengar)
    elif t1==t2==t3:
        print ("vinst + 50 kr")
        pengar = pengar +50
        print (" Kvar att spela för ", pengar)
    else:
        print ("förlust") 
        #pengar = pengar -1
    print ("du har", pengar)
    fråga =input ("Skriv (j) för att spela och (n) för att sluta")
print ("Tack för att du spelade, välkommen åter!")
print ("klar")
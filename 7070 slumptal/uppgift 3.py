import random
fråga = input ("Skriv (j) för att spela och (n) för att sluta")
sten = 1
sax = 2
påse = 3
while fråga =="j":
    t1 = random.randrange (1, 4)
    if t1==1:
        print ("sten")
    elif t1==2:
        print ("sax")
    elif t1==3:
        print("påse")
    fråga = input ("Skriv (j) för att spela och (n) för att sluta")

svar = input("sten, sax eller påse")
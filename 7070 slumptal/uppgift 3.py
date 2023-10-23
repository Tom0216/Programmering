import random
fråga = input ("Skriv (j) för att spela och (n) för att sluta")
sten = 1
sax = 2
påse = 3


while fråga =="j":
    print("sten, sax eller påse")
    spelarval = input ("sten, sax or påse")

    t1 = random.randrange (1, 4)
    if t1==1:
        print ("sten")
    elif t1==2:
        print ("sax")
    elif t1==3:
        print("påse")

    if t1 == sten and spelarval == "påse":
        print ("spelarens alternativ: påse")
        print ("datorns alternativ: sten")
        print ("spelare vann")
    elif spelarval =="sten" and t1== påse:
        print ("Dator vann")
    elif t1== sax and spelarval == "sten":
        print ("spelare vann")
    elif spelarval == "sax" and t1 == sten:
        print ("Dator vann")
    elif t1== påse and spelarval == "sax":
        print ("spelare vann")
    elif t1== sax and spelarval== "påse":
        print ("Dator vann")
    fråga = input ("Skriv (j) för att spela och (n) för att sluta")
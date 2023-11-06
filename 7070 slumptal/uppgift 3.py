import random
fråga = input ("Skriv (j) för att spela och (n) för att sluta")
sten = 1
sax = 2
påse = 3
Du = 0
dator = 0

while fråga =="j":
    spelarval = input ("sten, sax eller påse")

    t1 = random.randrange (1, 4)
    if t1==1:
        print ("sten")
    elif t1==2:
        print ("sax")
    elif t1==3:
        print("påse")

    if t1 == sten and spelarval == "påse":
        print ("spelarens val: påse")
        print ("datorns val: sten")
        print ("spelare vann")
        Du = Du + 1
        dator = dator + 0
    elif spelarval =="sten" and t1== påse:
        print ("spelarens val: sten")
        print ("Datorns val: påse ")
        print ("Dator vann")
        Du = Du + 0
        dator = dator + 1
    elif t1== sax and spelarval == "sten":
        print ("spelarens val: sten")
        print ("datorns val: sax")
        print ("spelare vann")
        Du = Du + 1
        Dator = dator + 0
    elif spelarval == "sax" and t1 == sten:
        print ("spelarens val: sax")
        print ("datorns val: sten")
        print ("Dator vann")
        Du = Du + 0
        dator = dator + 1
    elif t1== påse and spelarval == "sax":
        print ("spelares val: sax")
        print ("datorns val: påse ")
        print ("spelare vann")
        Du = Du + 1
        dator = dator + 0
    elif t1== sax and spelarval== "påse":
        print ("spelarens val: påse")
        print ("datorns val: sax")
        print ("Dator vann")
        Du = Du + 0
        dator = dator + 1
    elif spelarval== "sten" and t1== sten:
        print ("spelarens val: sten")
        print ("datorns val: sten")
        print ("Lika, kör igen")
        Du = Du + 0
        dator = dator + 0
    elif spelarval== "påse" and t1== påse:
        print ("spelarens val: påse")
        print ("datorns val: påse")
        print ("Lika, kör igen")
        Du = Du + 0
        dator = dator + 0
    elif spelarval== "sax" and t1== sax:
        print ("spelarens val: sax")
        print ("datorn val: sax")
        print ("Lika, kör igen")
    Du = Du + 0
    dator = dator + 0
    print ("Dina poäng", Du)
    print ("Dator poäng", dator)
    fråga = input ("Skriv (j) för att spela och (n) för att sluta")
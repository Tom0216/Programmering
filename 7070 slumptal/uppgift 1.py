import random
"""
fråga =input ("Vill du spela? j/n")
import random
while fråga=="j":
    t1 = random.randrange(1,7)
    t2 = random.randrange (1, 7)
    print (t1, t2)
    if t1==t2:
        print("vinst")
    else:
        print("förlust")
    fråga =input ("Vill du spela? j/n")
print ("Vad roligt att du spelde en stund")
"""
"""
fråga =input ("Vill du spela? j/n")
import random
while fråga=="j":
    t1 = random.randrange(1,7)
    t2 = random.randrange (1, 7)
    print (t1, t2)
    if t1==t2:
        print("vinst")
    elif t1==6:
        print ("sex-vinst")
    elif t2==6:
        print ("sex-vinst")
    else:
        print("förlust")
    fråga =input ("Vill du spela? j/n")
print ("Vad roligt att du spelde en stund")
"""
"""
fråga =input ("Vill du spela? j/n")
import random
while fråga=="j":
    t1 = random.randrange(1,7)
    t2 = random.randrange (1, 7)
    print (t1, t2)
    if t1==t2:
        print("vinst")
    elif t1==6 or t2==6:
        print ("sex-vinst")

    elif t1==t2+1 or t2==t1+1:
        print ("steg-vinst")

    else:
        print("förlust")
    fråga =input ("Vill du spela? j/n")
print ("Vad roligt att du spelde en stund")

"""
fråga = print ("Välkommen att kasta tärning")
print ("Ett spel kostar en krona")
print ("vinstplan")
print ("två lika = 5 kr")
print("en sexa = 3 kr")
print("stege = 3 kr")
fråga =input ("Välj spela (s), sätt in pengar (i), eller avsluta (a)")
while fråga=="i":
    belopp = input ("ange belopp att sätta in.")
    print("Du har", belopp, "kronor att spela med")
    fråga =input ("Välj spela (s), sätt in pengar (i), eller avsluta (a)")
while fråga=="s":
    t1 = random.randrange(1,7)
    t2 = random.randrange (1, 7)
    print (t1, t2)
    if t1==t2:
        print ("vinst + 5 kr")
    elif t1==6 or t2==6:
        print ("sex-vinst + 3 kr")
        
    elif t1==t2+1 or t2==t1+1:
        print ("steg-vinst + 3 krs")
    else:
        print("förlust")
    fråga =input ("Välj spela (s), sätt in pengar (i), eller avsluta (a)")
print ("Vad roligt att du spelade en stund!")
print ("klar")
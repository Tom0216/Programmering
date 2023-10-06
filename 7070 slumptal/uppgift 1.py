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

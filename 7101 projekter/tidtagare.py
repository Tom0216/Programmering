# start tidtagare
# kolla vad klockan är
# visa tid som räknar upp
# stoppa tidtagare
# visa tid
import time


# tryck s och return för att start tidtagning
svar = input ("Tryck på return för att starta tidtagningen")
#print ("Din", tid, "startar nu")

start_tid = time.time()

while svar != "slut":
    print("Skriv slut för att avluta.")
    svar = input ("Tryck return för mellantid:")
    slut_tid = time.time()
    tid = slut_tid - start_tid
    print("tid: ", tid)

print ("Din tid är stoppad")
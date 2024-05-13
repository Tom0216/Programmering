import time
import winsound

# läs in hur lång tid

tid = input ("Hur lång tid vill du ha på din äggklocka?")
start = input ("Tryck på return för att starta äggklockan")

# kolla tiden nu
tid_nu = time.time()
# räkna ut sluttid
slut_tid = tid_nu + float (tid)

print(slut_tid - time.time())
# kolla varje sekund (cirka)
while slut_tid > time.time():
    # vila 1 sekund
    time.sleep(1)
    print("vänta")

# när tiden är mer än sluttiden ring
print ("ring")
winsound.Beep(440, 500)
import random

Ettor = ("Ettor")
Tvåor = ("Tvåor")
Treor = ("Treor")
Fyror = ("Fyror")
Femmor = ("Femmor")
Sexor = ("Sexor")
Bonus =  ("Bonus")
par= ("Ett par")
tvåpar= ("Två par")
tretal = ("Tretal")
fyrtal = ("Fyrtal")
litenstege = ("Lite stege")
storstege= ("Stor stege")
Kåk= ("Kåk")
Chans= ("Chans")
Yatsy= ("Yatsy")

tärningar = []
# upprepa 5 gånger
# kasta tärning (slumpa) lägg till i tärningar

slumptal = random.randrange(1, 7)
tärningar.append(slumptal)
slumptal = random.randrange(1, 7)
tärningar.append(slumptal)
slumptal = random.randrange(1, 7)
tärningar.append(slumptal)
slumptal = random.randrange(1, 7)
tärningar.append(slumptal)
slumptal = random.randrange(1, 7)
tärningar.append(slumptal)

print (tärningar)

# upprepa 5 gånger
# kasta tärning (slumpa) lägg till i tärningar


print("1. ettor")
print("2. tvåor")
print("3. treor")
print("4.fyror")
print ("5. femmor")
print ("6. sexor")

svar = input("välj: ")
if svar == "1":
    print("antal ettor:", tärningar.count(1))
elif svar == "2":
    print("antal tvåor:", tärningar.count(2))
elif svar == "3":
    print("antal treor:", tärningar.count (3))
elif svar == "4":
    print("antal fyror:", tärningar.count (4))
elif svar == "5":
    print("antal femmor:", tärningar.count (5))
elif svar == "6":
    print("antal sexor:", tärningar.count (6))

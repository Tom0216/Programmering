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
for i in range(1, 7):
    tärningar.append(i)
random.shuffle(tärningar)
print (tärningar)

print("1. ettor")
print("2. tvåor")
print("3. treor")
print("4.fyror")
print ("5. femmor")
print ("6. sexor")

svar = input("välj: ")
if svar == "1":
    ("antal ettor", tärningar.count(1))
elif svar == "2":
    ("antal tvår", tärningar.count(2))
elif svar == 3:
    ("antal treor", tärningar.count (3))
elif svar ==4:
    ("antalet fyror", tärningar.count (4))
elif svar == 5:
    ("antalet femmor", tärningar.count (5))
elif svar == 6:
    ("antalet sexor", tärningar.count (6))

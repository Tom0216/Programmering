import random
tärningar = [1]

for i in range (9):
    tärningar.append(random.randint(1,6))


tärningar.sort()
print("sorterad: ", tärningar)
print ("summa", sum (tärningar))
medel = sum(tärningar)//len(tärningar)
print ("medel: ", medel)
print("min: ", min(tärningar))
print("max: ", max(tärningar))
print("antal sexor", tärningar.count(6))

antal = [0]
for i in range(1, 7):
    antal.append(tärningar.count(i))
antal_flest = (max(antal))
# på vilken plats?

print("flest:", antal.index(antal_flest))
# max i antal
# vilket index? dvs tärningsögon
("antal ettor", tärningar.count(1))
("antal tvår", tärningar.count(2))
("antal treor", tärningar.count(3))
("antal fyror", tärningar.count(4))
("antal femmor", tärningar.count(5))
("antal sexor", tärningar.count(6))
import random
Kung= 10
Dam= 10
Knekt= 10
# kortlek
# blandad
# dra 2 kort
kortlek = []
for i in range(1, 11):
    kortlek.append(i)
    kortlek.append(i)
    kortlek.append(i)
    kortlek.append(i)
random.shuffle(kortlek)
print(kortlek)

hand = []


last = kortlek.pop()
hand.append(last)

last = kortlek.pop()

hand.append(last)

print(kortlek)
print (hand)
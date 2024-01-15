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

# ta bort sista kortet i kortlekten
# lägg det i last
last = kortlek.pop()
# lägg kortet i hand
hand.append(last)

# dra sista kortet i leken
last = kortlek.pop()
# lägg kortet i hand
hand.append(last) 
print (kortlek)   
print (hand)

# ge kort till dealern

fråga =  input ("vill du ha fler kort? j/n")
while fråga == "j":
    # få ett kort till
    last = kortlek.pop()
    hand.append(last)
    print (hand)
    fråga =  input ("vill du ha fler kort? j/n")
#while fråga == "n":

dealern = []
last = kortlek.pop()
dealern.append(last)
last = kortlek.pop()
dealern.append(last)
print (dealern)

#fråga =  input ("vill du ha fler kort? j/n")
# dealern tar ett nytt kort
# medan summan är mindre än 17
while sum (dealern) <17:
        last = kortlek.pop()
        dealern.append(last)
        print (dealern)

# vem vann?
if sum(hand) > sum (dealern) and sum (hand)<=21 or sum(dealern) >=21:
    print ("hand vinner")
else:
    if sum(hand) < sum (dealern) and sum (dealern)<=21:
        print ("dealern vann")
print ("hand summa:", sum (hand))
print ("dealern summa:", sum (dealern))

# om player score > dealer score => player wins
# annars dealer wins



# om ja -> ett kort till i hand
# om nej -> inga fler kort, dealerns tur

# dealern drar kort, fyller sin hand
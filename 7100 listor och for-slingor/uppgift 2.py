antal = [0]
for i in range(2, 101):
    är_primtal = True
    for delare in range(2, i):
        if i % delare == 0:
            är_primtal = False
    if (är_primtal):
        print(i)
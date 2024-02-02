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

sparade_alternativ = {'ettor' : -1, 'tvåor' : -1, 'treor' : -1, 'fyror' : -1, 'femmor': -1,'sexor':-1 }
print(sparade_alternativ)

for j in range(6):
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
    for i in range(2):
        # välj vilka tärningar som ska sparas
        print("1. ettor")
        print("2. tvåor")
        print("3. treor")
        print("4.fyror")
        print ("5. femmor")
        print ("6. sexor")

        svar = input("välj: ")
        if svar == "1":
            # [2, 1, 4, 1, 2]
            antal_ettor = tärningar.count(1)
            tärningar = []
            for i in range(antal_ettor):
                tärningar.append (1)
            # [1, 1]
            # kasta övriga
            for i in range (5-antal_ettor):
                slumptal = random.randrange(1, 7)
                tärningar.append(slumptal)
            print("debug", tärningar)
            print("antal ettor:", tärningar.count(1))
            print("1",tärningar.count(1) )
        elif svar == "2":
            # [2, 1, 4, 1, 2]
            antal_ettor = tärningar.count(1)
            tärningar = []
            for i in range(antal_ettor):
                tärningar.append (1)
            # [1, 1]
            # kasta övriga
            for i in range (5-antal_ettor):
                slumptal = random.randrange(1, 7)
                tärningar.append(slumptal)
            print("debug", tärningar)
            print("antal tvåor:", tärningar.count(2)) 
            print("2",  tärningar.count(2) * 2)
        elif svar == "3":
            # [2, 1, 4, 1, 2]
            antal_ettor = tärningar.count(1)
            tärningar = []
            for i in range(antal_ettor):
                tärningar.append (1)
            # [1, 1]
            # kasta övriga
            for i in range (5-antal_ettor):
                slumptal = random.randrange(1, 7)
                tärningar.append(slumptal)
            print("debug", tärningar)
            print("antal treor:", tärningar.count (3)) 
            print("3", tärningar.count (3) *3 )
        elif svar == "4":
            # [2, 1, 4, 1, 2]
            antal_fyror = tärningar.count(4)
            tärningar = []
            for i in range(antal_fyror):
                tärningar.append (4)
            # [1, 1]
            # kasta övriga
            for i in range (5-antal_fyror):
                slumptal = random.randrange(1, 7)
                tärningar.append(slumptal)
            print("debug", tärningar)
            print("antal fyror:", tärningar.count (4)) 
            print("4",tärningar.count (4)*4 )
        elif svar == "5":
            # [2, 1, 4, 1, 2]
            antal_femmor = tärningar.count(5)
            tärningar = []
            for i in range(antal_femmor):
                tärningar.append (5)
            # [1, 1]
            # kasta övriga
            for i in range (5-antal_femmor):
                slumptal = random.randrange(1, 7)
                tärningar.append(slumptal)
            print("debug", tärningar)
            print("antal femmor:", tärningar.count (5)) 
            print("5",tärningar.count (5)*5 )
        elif svar == "6":
            # [2, 1, 4, 1, 2]
            antal_sexor = tärningar.count(6)
            tärningar = []
            for i in range(antal_sexor):
                tärningar.append (6)
            # [1, 1]
            # kasta övriga
            for i in range (5-antal_sexor):
                slumptal = random.randrange(1, 7)
                tärningar.append(slumptal)
            print("debug", tärningar)
            print("antal sexor:", tärningar.count (6)) 
            print("6", tärningar.count (6) * 6 )


    # omgång 1 klar
    # välj vad det ska sparas som
    # meny
    # spara i variabel
    print("Vad vill du spara det som?")
    print("1. ettor")
    print("2. tvåor")
    print("3. treor")
    print("4.fyror")
    print ("5. femmor")
    print ("6. sexor")

    svar = input("välj: ")

    if svar == "1":
        sparade_alternativ ["ettor"] = tärningar.count (1) * 1
    if svar == "2":
        sparade_alternativ ["tvåor"] = tärningar.count (2) * 2
    if svar == "3":
        sparade_alternativ ["treor"] = tärningar.count (3) * 3
    if svar == "4":
        sparade_alternativ ["fyror"] = tärningar.count (4) * 4
    if svar == "5":
        sparade_alternativ ["femmor"] = tärningar.count (5) * 5
    if svar == "6":
        sparade_alternativ ["sexor"] = tärningar.count (6) * 6

    print(sparade_alternativ)



"""
    svar = input("välj: ")
    if svar == "1":
        print("antal ettor:", tärningar.count(1))
        print("1",tärningar.count(1) )
    elif svar == "2":
        print("antal tvåor:", tärningar.count(2)) 
        print("2",  tärningar.count(2) * 2)
    elif svar == "3":
        print("antal treor:", tärningar.count (3)) 
        print("3", tärningar.count (3) *3 )
    elif svar == "4":
        print("antal fyror:", tärningar.count (4)) 
        print("4",tärningar.count (4)*4 )
    elif svar == "5":
        print("antal femmor:", tärningar.count (5)) 
        print("5",tärningar.count (5)*5 )
    elif svar == "6":
        print("antal sexor:", tärningar.count (6)) 
        print("6", tärningar.count (6) * 6 )
"""

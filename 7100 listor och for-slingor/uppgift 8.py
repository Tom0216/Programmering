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

sparade_alternativ = {'ettor' : -1, 
                      'tvåor' : -1, 
                      'treor' : -1, 
                      'fyror' : -1, 
                      'femmor': -1,
                      'sexor':-1,
                      'bonus':-1,
                      'par':-1,
                      'tvåpar':-1,
                      'tretal':-1,
                      'fyrtal':-1,
                      'litenstege':-1,
                      'storstege':-1,
                      'kåk':-1,
                      'chans':-1,
                      'yatsy':-1,}
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
        ettor= print ==1
        tvåor= print ==2
        treor= print ==3
        fyror= print == 4
        femmor= print == 5
        sexor= print == 6


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
            antal_tvåor = tärningar.count(2)
            tärningar = []
            for i in range(antal_tvåor):
                tärningar.append (2)
            # [1, 1]
            # kasta övriga
            for i in range (5-antal_tvåor):
                slumptal = random.randrange(1, 7)
                tärningar.append(slumptal)
            print("debug", tärningar)
            print("antal tvåor:", tärningar.count(2)) 
            print("2",  tärningar.count(2) * 2)
        elif svar == "3":
            # [2, 1, 4, 1, 2]
            antal_treor = tärningar.count(3)
            tärningar = []
            for i in range(antal_treor):
                tärningar.append (3)
            # [1, 1]
            # kasta övriga
            for i in range (5-antal_treor):
                slumptal = random.randrange(1, 7)
                tärningar.append(slumptal)
            print("debug", tärningar)
            print("antal treor:", tärningar.count (3)) 
            print("3", tärningar.count (3) * 3)
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




    godkännt_val = False
    while not godkännt_val:
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
        print ("7. bonus")
        print ("8. 1 par")
        print ("9. 2 par")
        print ("10. 3 par")
        print ("11. triss")
        print ("12. fyrtal")
        print ("13. 2 triss")
        print ("14. liten stege")
        print ("15. stor stege")
        print ("16. royal flash")
        print ("17. kåk")
        print ("18. chans")
        print ("19. YATZY")

        svar = input("välj: ")
    
        if svar == "1":
            # bara möjligt om man inte har sparat ettor tidigare
            # väljer ettor en andra gång => gör om val
            if sparade_alternativ ["ettor"] == -1:
                sparade_alternativ ["ettor"] = tärningar.count (1) * 1
                godkännt_val = True
            else:
                # välj ett nytt alternativ
                gokännt_val = False
        if svar == "2":
            if sparade_alternativ ["tvåor"] == -1:
                sparade_alternativ ["tvåor"] = tärningar.count (2) * 2
                godkännt_val = True
            else:
                # välj ett nytt alternativ
                gokännt_val = False
        if svar == "3":
            if sparade_alternativ ["treor"] == -1:
                sparade_alternativ ["treor"] = tärningar.count (3) * 3
                godkännt_val = True
            else:
                gokännt_val = False
        if svar == "4":
            if sparade_alternativ ["fyror"] == -1:
                sparade_alternativ ["fyror"] = tärningar.count (4) * 4
                godkännt_val = True
            else:
                gokännt_val= False
        if svar == "5":
            if sparade_alternativ ["femmor"] == -1:
                sparade_alternativ ["femmor"] = tärningar.count (5) * 5
                godkännt_val = True
            else:
                gokännt_val= False
        if svar == "6":
            if sparade_alternativ ["sexor"] == -1:
                sparade_alternativ ["sexor"] = tärningar.count (6) * 6
                godkännt_val= True
            else:
                gokännt_val = False
        if svar == "7":
            if sparade_alternativ ["bonus"] == -1:
                sparade_alternativ ["bonus"] = tärningar.count (1-6) == 52
                godkännt_val = True
            else:
                gokännt_val == False
        if svar == "8":
            if sparade_alternativ ["1 par"] == -1:
                sparade_alternativ ["1 par"] = tärningar.count #?
                godkännt_val == True
            else:
                gokännt_val == False
        if svar == "9":
            if sparade_alternativ ["2 par"] == -1:
                sparade_alternativ ["2 par"] = tärningar.count #?
                godkännt_val == True
            else:
                gokännt_val == False
        print(sparade_alternativ)
print ("antal", sum (sparade_alternativ.values()))


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

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
litenstege = ("Litenstege")
storstege= ("Storstege")
Kåk= ("Kåk")
Chans= ("Chans")
Yatsy= ("Yatsy")

sparade_alternativ = {'ettor' : -1, 
                      'tvåor' : -1, 
                      'treor' : -1, 
                      'fyror' : -1, 
                      'femmor': -1,
                      'sexor':-1,
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

for j in range(16):
    tärningar = []
    # upprepa 5 gånger
    # kasta tärning (slumpa) lägg till i tärningar

    for k in range (5):
        slumptal = random.randrange(1, 7)
        tärningar.append(slumptal)
    


    print (tärningar)
    for i in range(2):
        # välj vilka tärningar som ska sparas
        att_spara = input ("Välj vilka tärningar du vill spara?")
        print("Jag vill spara", att_spara)
        # har text med siffror
        # översätt till lista med tal
        val = []
        for bokstav in att_spara:
            if bokstav.isdigit():
                tal = int(bokstav)
                # om tal finns bland tärningarna: så spara
                if tal in tärningar :

                    val.append(tal)
                    tärningar.remove(tal)

        print("jag vill spara: ", val)

        # kasta om övriga tärningar
        tärningar = val
        for k in range (5 - len(tärningar)):
            slumptal = random.randrange(1, 7)
            tärningar.append(slumptal)
        print("dina tärningar visar:", tärningar)

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
        print ("7. par")
        print ("8. tvåpar")
        print ("9. tretal")
        print ("10. fyrtal")
        print ("11. litenstege")
        print ("12. storstege")
        print ("13. kåk")
        print ("14. chans")
        print ("15. YATZY")

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
            if sparade_alternativ ["par"] == -1:
                # vad finns det par i?
                # finns det två sexor?
                # finns det två femmor? ...
                # inget par, vad gör vi då?
# TODO          
                for i in range(6,0, -1):
                    if tärningar.count(i) >= 2:              
                        sparade_alternativ ["par"] = i * 2
                
                if sparade_alternativ ["par"] > 0:
                    None # gör inget, poäng har delats ut
                else:
                    # inga poäng har delats ut
                    sparade_alternativ ["par"] = 0
                godkännt_val = True 
            else:
                gokännt_val = False
        if svar == "8":
            if sparade_alternativ ["tvåpar"] == -1:
                # räkna antal 6, 5, 4, ..., 1

                par_i = []
                # slinga som räknar 1, 2, 3, 4,5, 6
                for i in range (1, 7, 1):

                    # om antalet är minst 2: lägg till dessa tärningsögon i par_i
                    if tärningar.count(i)>= 2:
                        par_i.append(i)
                # två olika par - finns?
                if len(par_i) >= 2:
                    
                    sparade_alternativ ["tvåpar"] = par_i[0] * 2 + par_i[1] * 2
                    # har två par
                    # ge poäng

                godkännt_val = True
            else:
                gokännt_val = False
        if svar == "9":
            if sparade_alternativ ["tretal"] == -1:

                for i in range (6, 0, -1):
                    if tärningar.count(i) >= 3:
                        sparade_alternativ ["tretal"] = i * 3
                if sparade_alternativ["tretal"] > 0:
                    None
                else:
                    sparade_alternativ ["tretal"] = 0        
                godkännt_val = True 
            else:
                gokännt_val = False
        if svar == "10":
            if sparade_alternativ ["fyrtal"] == -1:

                for i in range (6, 0, -1):
                    if tärningar.count(i) >= 4:
                        sparade_alternativ ["fyrtal"] = i * 4
                if sparade_alternativ ["fyrtal"] > 0:
                    None
                else:
                    sparade_alternativ ["fyrtal"] = 0
                godkännt_val = True
            else:
                gokännt_val = False
        if svar == "11":
            if sparade_alternativ ["litenstege"] == -1:
                tärningar.sort()
                if (tärningar[0] == 1 and tärningar [1] == 2 and tärningar [2] == 3 
                    and tärningar [3] == 4 and tärningar [4] == 5):
                    sparade_alternativ ["litenstege"] = 15
                else:
                    sparade_alternativ ["litenstege"] = 0
                godkännt_val = True
            else:
                gokännt_val = False
        if svar == "12":
            if sparade_alternativ ["storstege"]  == -1:
                tärningar.sort()
                if (tärningar [0] == 2 and tärningar [1] == 3 and tärningar [2] == 4 and tärningar [3] == 5 and 
                    tärningar [4] == 6):
                    sparade_alternativ ["storstege"] = 20
                else:
                    sparade_alternativ ["storstege"] = 0
                godkännt_val = True
            else:
                gokännt_val = False
        if svar == "13":
            if sparade_alternativ ["kåk"] == -1:
                tärningar.sort()
                # tex 22 555
                # t.ex. 222 55
                
                if ((tärningar [0] == tärningar [1] and tärningar [2] == tärningar [3] == tärningar [4]) or 
                    (tärningar [0] == tärningar[1] == tärningar[2] and tärningar [3] == tärningar[4])):
                    sparade_alternativ ["kåk"] = sum(tärningar)
                else:
                    sparade_alternativ ["kåk"] = 0
                godkännt_val = True
            else:
                gokännt_val = False
        if svar == "14":
            if sparade_alternativ ["chans"] == -1:
                sparade_alternativ ["chans"] = sum (tärningar)
                godkännt_val = True
            else:
                gokännt_val = False
        if svar == "15":
            if sparade_alternativ ["yatsy"] == -1:
                if tärningar [0] == tärningar[1] == tärningar[2] == tärningar[3] == tärningar[4]:
                    sparade_alternativ["yatsy"] = 50
                else:
                    sparade_alternativ ["yatsy"] = 0
                godkännt_val = True
            else:
                gokännt_val = False


    print(sparade_alternativ)

#poäng
# 50 i bonus om summan av alla 1 - 6 är minst 63
    

bonus = 0
if  (sparade_alternativ["ettor"] + sparade_alternativ["tvåor"] + sparade_alternativ ["treor"] + 
     sparade_alternativ ["fyror"] + sparade_alternativ ["femmor"] + sparade_alternativ ["sexor"] >= 63):

    print ("bonus")
    bonus = 50
print ("antal", sum (sparade_alternativ.values()) + bonus)

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

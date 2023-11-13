text=input("Ange ett heltal")
tal = int(text)
if 0 <= tal and tal <= 9:
    print("ensiffriga tal")
elif 10<= tal and tal <= 99:
    print ("tvåsiffriga tal")
elif 100<= tal and tal <= 999:
    print ("tresiffriga tal")
elif 1000<= tal:
    print ("fyrsiffriga tal")
elif -1>= tal:
    print ("negativa tal")
print ("klar")

def är_jämnt (tal):
    if tal % 2 == 0:
        return True
    else:
        return False
    
mitt_tal = int(input("ange ett heltal: "))

if är_jämnt(mitt_tal):
    print("jämnt")
else:
    print("udda")


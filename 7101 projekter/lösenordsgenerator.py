import random

tecken = "15928349"


kod = input ("Hur många siffror vill du ha i lösenordet?")
kod = int(kod)
print("Jag vill ha", kod,  "i lösenordet" "!")

for i in range(kod):
    bokstav = random.choice(tecken)
    print(bokstav, end='')


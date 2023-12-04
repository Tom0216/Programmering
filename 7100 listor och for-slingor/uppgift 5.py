

import random
t1 = [(random.randint(1,6))]

for i in range(4):
    t1.append(random.randint(1,6))
print ("",t1 ,"")
t1.sort()
print("antal ettor", t1.count(1))


if t1[0] == t1[1] and t1[0] == t1[2] and t1[0]==[3] and t1[0] ==t1[4]:
    print ("yatsy 50")
else:
    print ("inte yatsy")

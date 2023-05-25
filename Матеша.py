import random
c = 0

while (c != 4):
    one = random.randint(1, 9)
    two = random.randint(1, 9)
    itog = input(str(one) + "+" + str(two) + "=")
    if int(itog) == (one + two):
        print("Харош!")
    elif int(itog) != (one + two):
        c += 1
        print("Плох...")
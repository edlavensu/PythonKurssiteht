import random

oikea_luku = random.randint(1,10)

while True:
    arvaus = int(input("arvaa luku 1-10: "))

    if arvaus < oikea_luku:
        print("Liian pieni")
    elif arvaus > oikea_luku:
        print("Liian suuri")
    else:
        print("Oikein")
        break
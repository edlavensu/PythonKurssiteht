import random
def heita_noppa():
    return random.randint(1,6)

def main():
    tulos = 0
    while tulos !=6:
        tulos = heita_noppa()
        print("heitit: {tulos}")

main()
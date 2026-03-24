import random

def heita_muokattu_noppaa(tahkot):
    return random.randint(1, tahkot)

def main():
    tahkojen_maara = int(input("Kuinka monta tahkoa nopassa on?"))
    tulos = 0
    while tulos != tahkojen_maara:
        tulos = heita_muokattu_noppaa(tahkojen_maara)
        print(f"heitit: {tulos}")

main()

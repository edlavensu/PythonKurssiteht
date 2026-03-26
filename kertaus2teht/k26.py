def summa(a, b):
    return a + b

def erotus(a, b):
    return a - b

def tulo(a, b):
    return a * b

def jako(a, b):
    return a / b


print("käytä laskinta!")

while True:
    print("\nValitse mitä toimintoa haluat käyttää:")
    print(" A: Yhteenlasku")
    print(" B: Vähennyslasku")
    print(" C: Kertolasku")
    print(" D: Jakolasku")

    valinta = input("Valintasi (A-D, Q lopettaa): ")

    if valinta == "Q":
        print("Hei hei!")
        break

    if valinta in ["A", "B", "C", "D"]:
        a = float(input("Anna ensimmäinen luku: "))
        b = float(input("Anna toinen luku: "))

        if valinta == "A":
            print("Tulos:", summa(a, b))

        elif valinta == "B":
            print("Tulos:", erotus(a, b))

        elif valinta == "C":
            print("Tulos:", tulo(a, b))

        elif valinta == "D":
            if b == 0:
                print("Ei voi jakaa nollalla!")
            else:
                print("Tulos:", jako(a, b))
    else:
        print("Virheellinen valinta!")
while True:
    print("1 = yhteenlasku")
    print("2 = vähennys")
    print("3 = kertolasku")
    print("4 = jakolasku")
    print("0 = lopeta")

    valinta = input("valitse toiminto: ")

    if valinta == "0":
        print("Ohjelma lopetettu")
        break
    luku1= float(input("Anna ensimmäinen luku: "))
    luku2= float(input("Anna toinen luku: "))

    if valinta == "1":
        print("tulos: ", luku1 + luku2)
    elif valinta == "2":
        print("tulos: ", luku1 - luku2)
    elif valinta == "3":
        print("tulos: ", luku1 * luku2)
    elif valinta == "4":
        print("tulos: ", luku1 / luku2)
    else:
        print("Virheellinen valinta")
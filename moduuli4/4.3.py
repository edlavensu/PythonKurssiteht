annettu = input("Anna luku (tyhjä lopettaa)")

if annettu == "":
    print(" et syöttänyt yhtään lukua")
else:
    pienin = float(annettu)
    suurin = float(annettu)

    while True:
        annettu = input("anna luku (tyhjä lopettaa): ")
        if syöte == "":
            break
    luku = float(annettu)

    if luku < pienin:
        pienin = luku
    if luku > suurin:
        suurin = luku
    print("pienin luku", pienin)
    print("suurin luku", suurin)

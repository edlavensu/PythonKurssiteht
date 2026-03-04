tarina = (" ")
edellinen = (" ")

while True:
    sana = input("Anna sana lisättäväksi tarinaan: ")

    if sana == "loppu" or sana == edellinen:
        print(tarina)
        break

    tarina = tarina + sana + " "
    edellinen = sana
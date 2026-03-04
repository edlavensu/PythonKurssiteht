tuntipalkka = float(input("Tuntipalkka: "))
tunnit = float(input("tehdyt tunnit: "))
paiva = input("viikonpäivä: ")

if paiva == "sunnuntai":
    palkka = tuntipalkka * 2 * tunnit
else:
    palkka = tuntipalkka * tunnit

print("päiväpalkka:", palkka, "euroa")
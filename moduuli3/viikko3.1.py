pituus = float(input("Anna kuhan pituus cm:"))

if pituus < 37:
    puuttuu = 37 - pituus
    print("Laita kuha takaisin järveen")
    print("Puuttuu", puuttuu, "cm sallitusta mitasta")
else:
    print("Kuha on tarpeeksi pitkä")
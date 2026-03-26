lista = ["kissa", "tietokone", "auto", "kirjasto", "omena"]

sanat= 0

for sana in lista:
    if len(sana) > 5:
        sanat += 1

print(f"Listassa {sanat} sanassa on yli 5 kirjainta")
oikea_tunnus = "edlu"
oikea_salasana = "kassu"

yritykset = 0

while yritykset < 5 :
    tunnus = input("Käyttäjätunnus: ")
    salasana = input("Salasana: ")

    if tunnus == oikea_tunnus and salasana == oikea_salasana:
        print("Tervetuloa!")
        break
    else:
        print("Väärä tunnus tai salasana")
        yritykset += 1
if yritykset == 5:
    print("pääsy evätty")
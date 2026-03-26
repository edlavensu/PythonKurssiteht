lista = []

while True:
    luku = int(input("Uusi arvo: "))

    if luku == 0:
        print("Hei hei!")
        break

    lista.append(luku)

    print("Lista nyt:", lista)
    print("Lista järjestyksessä:", sorted(lista))
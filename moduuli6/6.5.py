def karsi_parittomat(lista):
    # Luodaan uusi lista, jossa on on vain parilliset (jakojäännös 2:lla on =0)
    return [luku for luku in lista if luku % 2 == 0]

def main():
    alkuperainen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    karsittu = karsi_parittomat(alkuperainen)

    print(f"karsittu lista: {alkuperainen}")
    print(f"Karsittu lista (vain parilliset): {karsittu}")

main()

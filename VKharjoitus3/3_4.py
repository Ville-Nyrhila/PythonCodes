__author__ = 'Ville'

def lue_syöte(kys):
    luku = -1
    while luku <= 0:
        luku = input(kys)
        luku = int(luku)
    return luku

def tulosta_ruutu(l,k,m):
    for i in range(k):
        print(m * l)

def main():

    leveys = lue_syöte("Syötä ruudun leveys: ")
    korkeus = lue_syöte("Syötä ruudun korkeus: ")
    merkki = input("Syötä tulostusmerkki: ")

    tulosta_ruutu(leveys, korkeus, merkki)

main()

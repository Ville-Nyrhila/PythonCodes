__author__ = 'Ville'

def tulosta_ruutu(l, k, m):
    for i in range(k):
        print(m * l)

def main():
    rivi = input("Syötä ruudun leveys: ")
    leveys = int(rivi)
    rivi = input("Syötä ruudun korkeus: ")
    korkeus = int(rivi)
    merkki = input("Syötä tulostusmerkki: ")

    tulosta_ruutu(leveys, korkeus, merkki)


main()
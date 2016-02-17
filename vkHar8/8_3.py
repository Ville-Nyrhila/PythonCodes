__author__ = 'Ville'

def main():
    nimi = input("Syötä tiedoston nimi: ")
    try:
        tiedosto = open(nimi, "r")
    except FileNotFoundError:
        print("Virhe! Tiedostoa {} ei saada luettua.".format(nimi))
        return 0
    lista = []
    luku = 0
    for rivi in tiedosto:
        try:
            rivi.rstrip()
            luku = int(rivi)
            lista.append(luku)
        except ValueError:
            print("Virhe! Tiedosto {} ei sisällä pelkkiä numeroita.".format(nimi))
            return 0

    lista = sorted(lista)
    print("Opiskelijanumerot järjestettynä:")
    for rivi in lista:
        print(rivi)
#
main()
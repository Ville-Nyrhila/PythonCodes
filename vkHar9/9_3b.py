__author__ = 'Ville'


def loppuiko( taulu = [] ):
    pelaaja = None

    # vaakaviivat
    for rivi in taulu:

        if rivi[0] != ".":

            if rivi[0] == rivi[1] and rivi[1] == rivi[2]:
                pelaaja = rivi[0]
                return pelaaja

    # vinoviiva
    if taulu[0][0] != ".":
        if taulu[0][0] == taulu[1][1] and taulu[1][1] == taulu[2][2]:
            pelaaja = taulu[0][0]
            return pelaaja

    # toinen vinoviiva
    if taulu[0][2] != ".":
        if taulu[0][2] == taulu[1][1] and taulu[1][1] == taulu[2][0]:
            pelaaja = taulu[0][2]
            return pelaaja

    #pystyviivat
    for i in range(3):
        if taulu[0][i] != ".":
            if taulu[0][i] == taulu[1][i] and taulu[1][i] == taulu[2][i]:
                pelaaja = taulu[0][i]
                return pelaaja
    return pelaaja
#
def main():

    # TODO luo pelilaudan tietorakenne
    lauta = []
    eka = [".", ".", "."]
    toka = [".", ".", "."]
    kolmas = [".", ".", "."]
    lauta.append(eka)
    lauta.append(toka)
    lauta.append(kolmas)

    voittaja = ""

    vuorot = 0  # Pelattujen vuorojen määrä

    # Peli jatkuu kunnes ruudukko on täynnä.
    # 8 vuoron vaihdon jälkeen laudalle on laitettu 9 merkkiä.
    while vuorot < 9:

        # Päivitetään merkki vuoron mukaan
        if vuorot % 2 == 0:
            merkki = "X"
        else:
            merkki = "O"
        koordinaatit = input("Pelaaja " + merkki + " anna koordinaatit: ")

        try:
            x, y = koordinaatit.split(" ")
            x = int(x)
            y = int(y)

            # TODO toteuta pelaajan vuoro
            if lauta[y][x] == ".":
                lauta[y][x] = merkki

                for rivi in lauta:
                    print(rivi[0] + rivi[1] + rivi[2])

                vuorot += 1
            else:
                print("Virhe: ruutuun on jo pelattu.")

        except ValueError:
            print("Virhe: syötä kaksi kokonaislukua välilyönnillä erotettuna.")

        except IndexError:
            print("Virhe: koordinaattien oltava välillä 0-2.")

        voittaja = loppuiko( lauta )
        if voittaja != None:
            print("Peli loppui, voittaja on " + voittaja)
            break
        if vuorot == 9:
            print("Tasapeli!")

main()
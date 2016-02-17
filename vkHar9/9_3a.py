__author__ = 'Ville'

def main():

    # TODO luo pelilaudan tietorakenne
    lauta = []
    eka = [".", ".", "."]
    toka = [".", ".", "."]
    kolmas = [".", ".", "."]
    lauta.append(eka)
    lauta.append(toka)
    lauta.append(kolmas)

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


main()
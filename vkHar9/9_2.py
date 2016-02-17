__author__ = 'Ville'

def lue_tiedosto(tiedoston_nimi):
    """Lukee ja tallentaa tiedostossa olevat sarjat ja niiden genret."""

    # TODO alusta tietorakenne
    sanakirja = {}
    lista = []

    try:
        tiedosto = open(tiedoston_nimi, "r")

        for rivi in tiedosto:
            lista = []
            # Erotellaan nimi ja genret erilleen
            # nimi on merkkijono ja genret lista
            nimi, genret = rivi.rstrip().split(";")
            genret = genret.split(",")

            # TODO lisää tieto tietorakenteeseen
            for genre in genret:
                if genre in sanakirja:
                    lista = sanakirja[genre]
                    if nimi not in lista:
                        lista.append(nimi)
                else:
                    lista = []
                    lista.append(nimi)
                    sanakirja[genre] = lista

        return  sanakirja # TODO palauta tietorakenne

    except ValueError:
        print("Virhe: rivi ei ole muotoa nimi;genret.")
        return None

    except IOError:
        print("Virhe: tiedostoa ei saada luettua.")
        return None


def main():

    tiedoston_nimi = input("Anna tiedoston nimi: ")
    sanakirja = lue_tiedosto(tiedoston_nimi)

    # TODO tulosta genrelista
    lajit = ""
    for avain in sorted(sanakirja):
        lajit += avain + ", "
    lajit = lajit[:-2]
    print("Valittavia genrejä ovat: " + lajit)

    lista = []

    while True:
        genre = input("> ")

        if genre == "lopeta":
            return

        # TODO sarjojen tulostus
        elif genre in sanakirja:
            lista = sanakirja[genre]
            for nimi in sorted(lista):
                print(nimi)

main()
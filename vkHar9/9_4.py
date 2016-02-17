__author__ = 'Ville'

def laske_prosentit( kertoimet = [], lista = [] ):
    summa = 0
    max = 0
    for i in range(len(kertoimet)):
        summa += int(kertoimet[i]) * int(lista[i])
        max += int(lista[i]) * 5

    return ( (summa / max) * 100)

#
def lue_tiedosto(tiedoston_nimi):
    """Lukee tiedostosta pelaajien pelaamat biisit ja saadut tulokset."""


    try:
        tiedosto = open(tiedoston_nimi, "r")

        # TODO: Määrittele käyttämäsi tietorakenne tänne
        laulutPisteet = {}
        laulajat = {}

        # Käydään tiedosto riveittäin läpi, rivi sisältää pelaajan tiedot
        for rivi in tiedosto:
            osat = rivi.strip().split(";")
            pelaaja = osat[0] # sisältää pelaajan nimen
            biisit = osat[1:] # jokainen listan alkio sisältää yhden biisin

            # TODO luo pelaajalle tietorakenne joka sisältää
            # pelaajan pelaamat kappaleet ja niiden tulokset
            if pelaaja not in laulajat:
                laulajat[pelaaja] = {}
                laulutPisteet = laulajat[ pelaaja ]
            else:
                laulutPisteet = laulajat[ pelaaja ]

            # Käydään läpi pelaajan pelaamat kappaleet yksi kerrallaan
            for biisi in biisit:
                osat = biisi.split(":")
                tulokset = osat[1].split(",")
                # Sisältää kappaleen nimen
                nimi = osat[0]
                # Sisältää listan kappaleen painalluksista (int)
                tulokset = [int(luku) for luku in tulokset]

                #TODO: Yhdistä tulokset kappaleen nimeen
                if nimi not in laulutPisteet:
                    laulutPisteet[ nimi ] = tulokset

                # TODO: Lisää kappaleet ja tulokset sisältävä tietorakenne
                # pelaajat sisältävään tietorakenteeseen.

        return  laulajat# TODO palauta tietorakenne

    except IOError:
        print("Virhe: tiedostoa ei saatu luettua.")
        return None


def main():

    kertoimet = [5, 4, 2, 0, -6, -12]

    tiedoston_nimi = input("Anna tiedoston nimi: ")
    laulajat = lue_tiedosto(tiedoston_nimi)
    sanakirja = {}
    pisteet = []
    pros = 0.0

    # TODO lisää tulostus
    for pelaaja in sorted(laulajat):
        print(pelaaja + ":")
        sanakirja = laulajat[ pelaaja ]
        for biisi in sorted(sanakirja):
            pros = laske_prosentit(kertoimet, sanakirja[ biisi ])
            print("\t" + biisi + ": {:.2f}%".format(pros))

#
main()
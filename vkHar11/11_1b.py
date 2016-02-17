__author__ = 'Ville'

class Murtoluku:
    """ Kuvaa yhtä murtolukua, joka koostuu osoittajasta ja nimittäjästä."""

    def __init__(self, osoittaja, nimittäjä):
        """
        Luokan rakentaja. Tarkastaa että osoittaja ja nimittäjä ovat
        kokonaislukuja ja alustaa ne annettuihin arvoihin.

        :param osoittaja: murtoluvun osoittaja
        :param nimittäjä: murtoluvun nimittäjä
        """

        if not isinstance(osoittaja, int) or not isinstance(nimittäjä, int):
            raise TypeError
        elif nimittäjä == 0:
            raise ValueError

        self.__osoittaja = osoittaja
        self.__nimittäjä = nimittäjä

    def sievennä(self):
        a = suurin_yhteinen_tekijä(self.__nimittäjä, self.__osoittaja)
        self.__nimittäjä /= a
        self.__nimittäjä = int(self.__nimittäjä)
        self.__osoittaja /= a
        self.__osoittaja = int(self.__osoittaja)

    def print_Vastaluku(self):
        if self.__osoittaja * self.__nimittäjä < 0:
            etumerkki = ""
        else:
            etumerkki = "-"
        print("{:s}{:d}/{:d}".format(etumerkki, abs(self.__osoittaja),
                                     abs(self.__nimittäjä)))

    def print_Käänteisluku(self):
        if self.__osoittaja * self.__nimittäjä < 0:
            etumerkki = "-"
        else:
            etumerkki = ""
        print("{:s}{:d}/{:d}".format(etumerkki, abs(self.__nimittäjä),
                                     abs(self.__osoittaja)))

    def tulosta(self):
        """ Tulostaa murtoluvun muodossa osoittaja/nimittäjä. """

        if self.__osoittaja * self.__nimittäjä < 0:
            etumerkki = "-"
        else:
            etumerkki = ""
        print("{:s}{:d}/{:d}".format(etumerkki, abs(self.__osoittaja),
                                     abs(self.__nimittäjä)))


def suurin_yhteinen_tekijä(a, b):
    """ Euklideen algoritmi kahden kokonaisluvun a ja b suurimman yhteisen
    tekijän laskemiseksi.  Kopioitu pääosiltaan internetistä. Algoritmin
    ymmärtäminen ei ole kurssilla tarpeen.
    """

    while b != 0:
        a, b = b, a % b
    return a


def main():
    try:
        rivi = input("Syötä murtoluku muodossa kokonaisluku/kokonaisluku: ")

        rivin_osat = rivi.split("/")
        if len(rivin_osat) != 2:
            raise ValueError

        mluku1 = Murtoluku(int(rivin_osat[0]), int(rivin_osat[1]))

    except:
        print("Virheellinen syöte!")
    else:
        # Tämä suoritetaan, jos try-lohko suoritettiin loppuun ilman poikkeusta
        print("Syöttämäsi murtoluku ", end="")
        mluku1.tulosta()
        mluku1.sievennä()
        print("Sievennetty muoto ", end="")
        mluku1.tulosta()
        print("Vastaluku ", end="")
        mluku1.print_Vastaluku()
        print("Käänteisluku ", end="")
        mluku1.print_Käänteisluku()


main()

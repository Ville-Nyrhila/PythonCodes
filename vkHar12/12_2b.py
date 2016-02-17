__author__ = 'Ville'

def suurin_yhteinen_tekijä(a, b):
    """ Euklideen algoritmi kahden kokonaisluvun a ja b suurimman yhteisen
    tekijän laskemiseksi.  Kopioitu pääosiltaan internetistä. Algoritmin
    ymmärtäminen ei ole kurssilla tarpeen.
    """

    while b != 0:
        a, b = b, a % b
    return a
#
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

    def __lt__(self, other):
        oso1 = self.gib_oso() * other.gib_nimit()
        oso2 = other.gib_oso() * self.gib_nimit()
        if oso1 < oso2:
            return True
        else:
            return False
    def __gt__(self, other):
        return other < self

    def __eq__(self, other):
        oso1 = self.gib_oso() * other.gib_nimit()
        oso2 = other.gib_oso() * self.gib_nimit()
        if oso1 == oso2:
            return True
        else:
            return False

    def __str__(self):
        if self.__osoittaja * self.__nimittäjä < 0:
            etumerkki = "-"
        else:
            etumerkki = ""
        return "{:s}{:d}/{:d}".format(etumerkki, abs(self.__osoittaja),
                                     abs(self.__nimittäjä))


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
    def gib_oso(self):
        return self.__osoittaja
    def gib_nimit(self):
        return self.__nimittäjä
    def gib_form(self):
        return str(self.__osoittaja) + "/" + str(self.__nimittäjä)
#
def main():
    syöte = ""
    luku = ""
    palat = []
    sanakirja = {}
    nimi = ""

    while syöte != "lopeta":
        syöte = input("> ")

        if syöte == "lisää":
            luku = input("Syötä murtoluku muodossa kokonaisluku/kokonaisluku: ")
            palat = luku.split("/")
            oso = int(palat[0])
            nimit = int(palat[1])
            nimi = input("Syötä nimi: ")
            sanakirja[ nimi ] = Murtoluku( oso, nimit)
        elif syöte == "lopeta":
            pass
        elif syöte == "tulosta":
            nimi = input("Syötä nimi: ")
            if nimi in sanakirja:
                print(nimi,"=",sanakirja[ nimi ])
            else:
                print("Nimeä x ei ole olemassa")
        else:
            print("Tuntematon komento!")

    print("Hei hei!")
#
main()
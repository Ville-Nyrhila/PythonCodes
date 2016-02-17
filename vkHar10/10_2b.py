__author__ = 'Ville'

TILANNETEKSTI = "Koordinaatit x={}, y={}, " \
    + "tankissa on {:.1f} litraa polttoainetta."


class Auto:
    """ Kuvaa kaksiulotteisessa koordinaatiostossa liikkuvaa autoa.
    ============
    Luokka siis määrittelee, millainen auto on: mitä tietoja se sisältää ja
    mitä toimenpiteitä se voi suorittaa.
    """

    def __init__(self, tankin_koko, kulutus):
        """ Alustaa olion alkutilaan (tankin koko ja kulutus halutuiksi)
        :param tankin_koko: auton tankin koko
        :param kulutus:  auton kulutus yhden kilometrin matkalla

        (Pythonissa rakentajan nimi on aina __init__. Rakenta on metodi, jota
        kutsutaan, kun luokasta halutaan luoda uusi olio, ks. rivi 40.
        Rakentaja alustaa uuden olion sisältämät kentät (tässä muuttujat
        self.__tankin_koko ja self.__kulutus) oikeisiin alkuarvoihin.
        """
        self.__tankin_koko = tankin_koko
        self.__kulutus = kulutus
        self.__x = 1
        self.__y = 1
        self.__tankki = 0

        # TODO: Lisää tähän uusien metodien määrittelyt.
        # Koska metodit ovat osa luokkaa, ne sisennetään samoin kuin yllä
        # oleva rakentaja.
    def tulosta_tilanne(self):
        print(TILANNETEKSTI.format(self.__x, self.__y, self.__tankki))
    def __gibTankki__(self):
        return self.__tankki
    def __gib_X__(self):
        return  self.__x
    def __gib_Y__(self):
        return self.__y
    def __tankkaa__(self, maara):
        self.__tankki += maara
        if self.__tankki > self.__tankin_koko:
            self.__tankki = self.__tankin_koko
    def __move__(self, komento):
        if komento == "P":
            self.__y += 1
        elif komento == "E":
            self.__x += 1
        elif komento == "S":
            self.__y -= 1
        elif komento == "W":
            self.__x -= 1

def main():

    kartan_koko = int(lue_luku("Syötä kartan koko: "))         # kokonaisluku
    tankin_koko = lue_luku("Syötä tankin koko: ")              # desimaaliluku
    kulutus = lue_luku("Syötä auton kulutus per kilometri: ")  # desimaaliluku

    # Tässä määritellään muuttuja auto, joka on luokan Auto olio. Tämä on
    # siis se kohta, jossa luokan Auto rakentajaa (__init__) kutsutaan!
    auto = Auto(tankin_koko, kulutus)
    # (Tässä ohjelmassa tarvitsemme vain yhden auton, mutta luokasta on
    # mahdollista luoda useampia olioita. Esim. pikkumatin_auto = Auto(10, 10)
    # ja pikkupekan_auto = Auto(20, 30). Tällöin jokaisella oliolla on omat
    # kenttänsä (self.__tankin_koko ja self.__kulutus_satasella), joilla voi
    # olla eri arvot, mutta oliot toimivat samalla tavalla, koska olion
    # toiminnan määrittelee luokka.)

    while True:

        auto.tulosta_tilanne()

        komento = input("Anna komento T/P/I/E/L/K/Q: ")
        komento = komento.upper()

        if komento == "T":
            tankataan = lue_luku("Montako litraa tankataan: ")
            # TODO Lisää tähän tankkaa-metodin kutsu
            auto.__tankkaa__( tankataan )

        elif komento in "PIEL" and len(komento) == 1:
            # TODO Lisää tähän aja-metodin kutsu
            auto.__move__(komento)

        elif komento == "K":
            # TODO Lisää tähän tulosta_kartta funktion kutsu
            pass

        elif komento == "Q":
            return

        else:
            print("Virhe: tuntematon komento")


def lue_luku(kehote, virheilmoitus="Vääräntyyppinen syöte!"):
    """ Lukee käyttäjältä syötettä, kunnes käyttäjän antama syöte on
    positiivinen luku. Sinun ei tarvitse muokata tätä funktiota eikä ymmärtää
    sen toimintaa, mutta voit halutessasi tutustua siihen.
    """

    try:
        return float(input(kehote))
    except ValueError:
        print(virheilmoitus)
        return lue_luku(kehote, virheilmoitus)


main()

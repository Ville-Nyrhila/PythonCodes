__author__ = 'Ville'

class Kulkukortti:

    def __init__(self, tunniste, nimi):
        """ Luokan rakentaja
        :param tunniste: henkilön tunniste (str)
        :param nimi: henkilön nimi (str)
        """
        self.__tunniste = tunniste
        self.__nimi = nimi
        self.__alueet = []

    def tulosta_tiedot(self):
        """ Funktiolla ei ole paluuarvoa. Se tulostaa kulkukortin
        tiedot näytölle täsmälleen seuraavassa muodossa:
        tunniste, nimi, kulkualueet: ka1,ka2,...,kaN
        eli esimerkiksi:
        567890, Siiri Siivooja, kulkualueet: F,K,P,R,S,T
        Huomaa, että pilkkujen ja kaksoispisteen perässä
        tulevien välilyöntien on oltava tulosteessa juuri
        saman logiikan mukaisesti kuin edellä ja kulkualueiden
        on tulostuttava tehtävänannon määräämässä järjestyksessä.
        TÄMÄN METODIN TOIMINTA TESTATAAN ERIKSEEN AUTOMAATTITESTISSÄ,
        JOTEN TULOSTUASUN MUUTTAMINEN JOHTAA TESTIEN EPÄONNISTUMISEEN.
        """
        print( self )

    def anna_nimi(self):
        """ Palauttaa kulkukortille talletetun henkilön nimen."""
        return self.__nimi

    def tarkista_pääsy(self, ovi):
        """
        Tarkastaa pääseeko kulkukortilla ovesta.
        TÄMÄN METODIN TOIMINTA TESTATAAN ERIKSEEN AUTOMAATTITESTISSÄ,
        JOTEN PALUUARVOJEN MUUTTAMINEN JOHTAA TESTIEN EPÄONNISTUMISEEN.
        :param ovi: Ovi josta halutaan mennä läpi
        :return: True: ovi avautuu kulkukortille tallennetuilla oikeuksilla.
                 False: ovi ei avaudu kulkukortin oikeuksilla
        """
        for lupa in self.__alueet:
            if lupa in ovi:
                return True

        return False

    def lisää_kulkualue(self, uusi_alue):
        """
        Funktio lisää uuden alueen kulkukortin oikeuksiin tehtävänannossa
        määritellyn säännön mukaisesti. Funktio ei saa tulostaa näytölle mitään.
        TÄMÄN METODIN TOIMINTA TESTATAAN ERIKSEEN AUTOMAATTITESTISSÄ.
        MIKÄLI SE EI TOIMI MÄÄRITTELYN MUKAISESTI, TESTIT EPÄONNISTUVAT.
        :param uusi_alue: Lisättävä kulkualue
        """
        uusi = []
        vanhaOliIsompi = False
        if uusi_alue not in self.__alueet:
            for alue in self.__alueet:

                # Uusi lupa on laajempi kuin vanha(t).
                if uusi_alue in alue and len( uusi_alue ) < len( alue ):
                    uusi.append( uusi_alue )
                    break

                # Vanha lupa on laajempi kuin uusi.
                if alue in uusi_alue and len( alue ) < len( uusi_alue ):
                    vanhaOliIsompi = True
                    break

            if not vanhaOliIsompi:
                self.__alueet.append( uusi_alue )

        # Jos vastaan tuli lupa, joka on
        # sama mutta laajempi kuin jokin/jotkin
        # vanhat, korvataan se/ne tällä uudella.
        if len( uusi ) != 0:
            for alue in self.__alueet:

                if alue not in uusi:
                    if uusi_alue in alue:
                        pass
                    else:
                        uusi.append( alue )
            self.__alueet = uusi

    def yhdistä_kulkukortti(self, toinen_kortti):
        """ Yhdistää toinen_kortti-parametrin sisältämät kulkuoikeudet
        käsiteltävänä olevalle kortille. Toimintalogiikka määritelty
        tehtävänannossa.
        :param toinen_kortti: Kulkukortti, jonka kanssa oikeudet yhdistetään
        """
        lista = toinen_kortti.alueet()
        for paikka in lista:
            self.lisää_kulkualue( paikka )

    def __str__(self):
        palaute = "" + self.__tunniste + ", " + self.__nimi + ", kulkualueet: "
        self.__alueet = sorted( self.__alueet )
        for alue in self.__alueet:
            palaute +=  alue + ","

        palaute = palaute[:-1]
        return palaute

    def nimi(self):
        return self.__nimi

    def alueet(self):
        return self.__alueet
#
def lue_tiedosto():
    try:
        palaute = {}
        filu = open( "kulkutiedot.txt", "r", encoding="utf-8" )

        for rivi in filu:

            # Rivin formaatti on:
            #
            rivi = rivi.rstrip()
            palat = rivi.split(';')
            tunniste = palat[0]
            nimi = palat[1]
            kortti =  Kulkukortti( tunniste, nimi )

            paikat = palat[2].split(',')
            for paikka in paikat:
                kortti.lisää_kulkualue( paikka )

            palaute[ tunniste ] = kortti

        filu.close()
        return palaute
    except Exception:
        return None
#
def main():
    sanakirja = lue_tiedosto()

    if sanakirja != None:
        while True:
            rivi = input("komento> ")

            if rivi == "":
                break

            osat = rivi.split()
            käsky = osat[0]

            if käsky == "lista" and len(osat) == 1:
                lista = sorted( sanakirja )
                for alkio in lista:
                    sanakirja[ alkio ].tulosta_tiedot()


            elif käsky == "tiedot" and len(osat) == 2:
                tunniste = osat[1]
                try:
                    print( sanakirja[ tunniste ] )
                except Exception:
                    print("Virhe: tuntematon tunniste.")

            elif käsky == "kulku" and len(osat) == 3:
                tunniste = osat[1]
                huone = osat[2]
                try:
                    lupa = sanakirja[ tunniste ]
                    if not lupa.tarkista_pääsy( huone ):
                        print("Kortilla {} ( {} ) ei kulkuoikeutta huoneeseen {}".format(tunniste, lupa.nimi() ,huone) )

                    elif lupa.tarkista_pääsy( huone ):
                        print("Kortilla {} ( {} ) on kulkuoikeus huoneeseen {}".format(tunniste, lupa.nimi() ,huone) )

                    else:
                        print("Virhe: tuntematon tunniste.")

                except Exception:
                    print("Virhe: tuntematon tunniste.")

            elif käsky == "lisää" and len(osat) == 3:
                try:
                    tunniste = osat[1]
                    alue = osat[2]
                    lupa = sanakirja[ tunniste ]
                    lupa.lisää_kulkualue( alue )
                except Exception:
                    print("Virhe: tuntematon tunniste.")

            elif käsky == "yhdistä" and len(osat) == 3:
                henkilö = osat[1]
                kortti = osat[2]

                try:
                    henkilö = sanakirja[ henkilö ]
                except Exception:
                    henkilö = None
                try:
                    kortti = sanakirja[ kortti ]
                except Exception:
                    kortti = None

                if henkilö != None and kortti != None:
                    henkilö.yhdistä_kulkukortti( kortti )
                else:
                    print("Virhe: tuntematon tunniste.")

            else:
                print("Virhe: Väärä syöte, yritä uudelleen")
    else:
        print("Virhe: tiedostoa ei saa luettua.")

#
main()

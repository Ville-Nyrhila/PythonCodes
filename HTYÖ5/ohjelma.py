__author__ = 'Ville'

import math

def lue_biometriikkarekisteri(tiedoston_nimi):
    """ Funktio lukee biometrisen informaation tehtävänannon määrämässä muodossa
    olevasta tiedostosta. Luettu informaatio jäsennellään ja talletetaan
    tietorakenteeseen, jonka harjoitustyön tekijä saa valita itse
    (ohjelmakoodissa tämä rakenne on nimetty muuttujaksi «tulos»).

    :param tiedoston_nimi: tiedoston nimi, josta biometrinen informaatio luetaan.
    :return: Palauttaa tietorakenteen, johon koko tiedosto on luettu ja tallennettu.
             Virhetilanteessa palauttaa arvon None.
    """

    # HUOMIOTAVAA:
    # (a) Kohtiin, joissa lukee TODO, ohjelmoijan on täytettävä jotain
    #     valitun tietorakenteen käsittelyyn liittyvää (kommenteissa vihjeitä).
    # (b) Tietorakenteen, jonka funktio palauttaa, on oltava jonkinlainen
    #     yhdistelmä sisäkkäisiä list- ja/tai dict-rakenteita. Se on koko
    #     harjoitustyön tavoite: sisäkkäisten tietorakenteiden käsittely.

    # TODO: Alustus: minkälaiseen rakenteeseen tiedoston sisältämä informaatio
    # olisi järkevää tallentaa?
    tulos = []
    sarake = []

    aiemmin_käsitellyt_passit = []

    try:
        with open(tiedoston_nimi, mode="r") as tiedosto_olio:
            for rivi in tiedosto_olio:
                rivi = rivi.rstrip()

                kentät = rivi.split(';')

                if len(kentät) != 8:
                    print("Virhe: syötetiedoston rivillä väärä määrä kenttiä:")
                    print("'", rivi, "'", sep="")
                    return None

                # Muutetaan listan lopussa viisi biometrista
                # arvoa merkkijonosta desimaaliluvuiksi.
                for indeksi in range(3, 8):
                    kentät[indeksi] = float(kentät[indeksi])
                    if not (0 <= kentät[indeksi] <= 3.0):
                        print("Virhe: tiedostossa virheellinen arvo rivillä:")
                        print("'", rivi, "'", sep="")
                        return None

                nimi = kentät[0] + ", " + kentät[1]
                passi = kentät[2]
                biometriikka = kentät[3:]
                bioni = []
                for bio in biometriikka:
                    bioni.append( float(bio) )

                if passi in aiemmin_käsitellyt_passit:
                    print("Virhe: passi nro.", passi, "toistuu.")
                    return None
                else:
                    aiemmin_käsitellyt_passit.append(passi)

                # TODO: Miten edellä luettu henkilön informaatio talletetaan
                # funktion alussa valittuun rakenteeseen?
                menee = []
                menee.append( nimi )
                menee.append( passi )
                menee.append( bioni )
                tulos.append( menee )
        return tulos

    except FileNotFoundError:
        print("Virhe: tiedostoa", tiedoston_nimi, "ei saa avattua.")

    except ValueError:
        print("Virhe: tiedostossa ei-numeerinen biomeriikka-arvo rivillä:")
        print("'", rivi, "'", sep="")

    return None

#
def ota_syöte():
    while(True):
        luvut_str = input("Syötä 5 mittausarvoa puolipisteellä eroteltuna: ")
        palat = luvut_str.split(";")
        if len(palat) != 5:
            print("Virhe: väärä määrä syötteitä: yritä uudelleen.")
            continue
        try:
            osat = []
            for osa in palat:
                osa = float(osa)
                osat.append( osa )
            return osat
        except ValueError:
            print("Virhe: syötä vain desimaalilukuja: yritä uudelleen.")
#
def vertailu( haku = [], verrokki = [] ):

    luvut2 = verrokki[2]

    nro = math.sqrt( (haku[0] - luvut2[0] )**2 + (haku[1] - luvut2[1] )**2 + (haku[2] - luvut2[2] )**2 \
                     + (haku[3] - luvut2[3] )**2 + (haku[4] - luvut2[4] )**2 )
    if nro < 0.1:
        return True

    return False
#
def vertaile_hlöä_rekisteriin(haku, biorekisteri, näkyyTyhjä = False, onHaku = False, hakuNimi = "", mainitut = {}, loydokset = 0):

    matchit = []
    loytyneet = []


    # Käydään biorekisteri läpi ja kopataan matchit.
    for henkilö in biorekisteri:
        if onHaku == False:
            if hakuNimi.split(";")[1] not in mainitut:
                if vertailu(haku, henkilö):
                    matchit.append( henkilö )
        else:
            if vertailu(haku, henkilö):
                matchit.append( henkilö )

    # Löytyi matcheja.
    if len( matchit ) != 0:
        if onHaku:
            print("Löytyi epäiltyjä:")
            for osui in matchit:

                    if osui[1] in mainitut:
                        pass
                    else:
                        mainitut[ osui[1] ] = True
                        luvut = osui[2]
                        viiva = "{};{};{:.2f};{:.2f};{:.2f};{:.2f};{:.2f}".format(osui[0], osui[1], luvut[0], \
                                                                                  luvut[1], luvut[2], luvut[3], \
                                                                                  luvut[4] )
                        loytyneet.append( viiva )
                        #loytyneet.append( osui[0] + ";" + osui[1] + ";" + str(luvut[0]) + ";" + str(luvut[1]) \
                        #                  + ";" + str(luvut[2]) + ";" + str(luvut[3]) + ";" + str(luvut[4]) )
            # Jos on löytynyt jotain.
            if len( loytyneet ) != 0:
                for kiva in loytyneet:
                    if kiva.rstrip() != "":
                        print(kiva)
                print()
            return
        else:
            tunnus = hakuNimi.split(";")[1]
            if not tunnus in mainitut:

                mainitut[ tunnus ] = True

                for osui in matchit:

                    if osui[1] in mainitut:
                        pass
                    elif osui[1] == tunnus:

                        hakuNimi = osui[0] + ";" + osui[1] + ";" + str(luvut[0]) + ";" + str(luvut[1]) \
                                   + ";" + str(luvut[2]) + ";" + str(luvut[3]) + ";" + str(luvut[4])
                    else:
                        mainitut[ osui[1] ] = True
                        luvut = osui[2]
                        viiva = "{};{};{:.2f};{:.2f};{:.2f};{:.2f};{:.2f}".format(osui[0], osui[1], luvut[0], \
                                                                                  luvut[1], luvut[2], luvut[3], \
                                                                                  luvut[4] )
                        loytyneet.append( viiva )
                        #loytyneet.append( osui[0] + ";" + osui[1] + ";" + str(luvut[0]) + ";" + str(luvut[1]) \
                        #                  + ";" + str(luvut[2]) + ";" + str(luvut[3]) + ";" + str(luvut[4]) )
                #
                # Jos on löytynyt jotain.
                if len( loytyneet ) != 0:

                    # Kopataan talteen oikea hakuNimi tulostettavaksi.
                    for rivi in biorekisteri:
                        if rivi[1] == tunnus:
                            hakuNimi = "{};{};{:.2f};{:.2f};{:.2f};{:.2f};{:.2f}".format( rivi[0], rivi[1], \
                                                                                       rivi[2][0], rivi[2][1], \
                                                                                       rivi[2][2], rivi[2][3], \
                                                                                       rivi[2][4])
                            #hakuNimi = rivi[0] + ";" + rivi[1] + ";" + str(rivi[2][0]) + ";" + str(rivi[2][1]) \
                            #           + ";" + str(rivi[2][2]) + ";" + str(rivi[2][3]) + ";" + str(rivi[2][4])
                            break

                    # Tulostetaan mahdolliset täsmäävät henkilöt.
                    print("Mahdollisesti samat henkilöt:")
                    if hakuNimi.rstrip() != "":
                        print(hakuNimi)
                    for kiva in loytyneet:
                        if kiva.rstrip() != "":
                            print(kiva)
                            loydokset += 1
                    print()

                # Palautetaan sanakirja. Tämä on tärkeää samat-komennossa.
                return mainitut, loydokset

    # Jos matcheja ei tullut.
    else:
        if näkyyTyhjä:
            print("Ei löytynyt epäiltyjä.")
            print()
        return mainitut, loydokset
#
def suorita_samat(biorekisteri):
    # TODO: Toteuta metodin toiminnallisuus tehtävänannon mukaisesti.
    sanakirja = {}
    loydokset = 0
    kirjoitettu = False
    for i in range( len( biorekisteri ) ):
        haku = biorekisteri[i][2]
        sanakirja, loydokset = vertaile_hlöä_rekisteriin( haku, biorekisteri,hakuNimi=(biorekisteri[i][0]+ ";" + biorekisteri[i][1]), mainitut=sanakirja )

        if loydokset != 0:
            kirjoitettu = True

    if not kirjoitettu:
        print("Ei samoja henkilöitä.")
#
def suorita_haku(biorekisteri):
    # TODO: Toteuta metodin toiminnallisuus tehtävänannon mukaisesti.
    haku = ota_syöte()
    vertaile_hlöä_rekisteriin( haku, biorekisteri, True, True )

#
def main():

    # Ohjelmoijan tehtävänänä on toteuttaa funktiot «suorita_samat» ja
    # ja «suorita_haku», joita valmiissa koodissa on kutsuttu.
    # Saattaa olla järkevää toteuttaa myös muita apufunktioita niiden avuksi.

    # HUOMIOTAVAA:
    # Tätä funktiota ei ole tarkoitus muokata.

    rekisteritiedosto = input("Syötä rekisteritiedoston nimi: ")

    biometriikkarekisteri = lue_biometriikkarekisteri(rekisteritiedosto)
    if biometriikkarekisteri is not None:

        while True:
            komento = input("komento [haku/samat/<enter>] ")
            if komento == "":
                return
            elif komento == "samat":
                suorita_samat(biometriikkarekisteri)
            elif komento == "haku":
                suorita_haku(biometriikkarekisteri)
            else:
                print("Virhe: tuntematon komento '", komento,
                      "': yritä uudelleen.", sep="")

main()
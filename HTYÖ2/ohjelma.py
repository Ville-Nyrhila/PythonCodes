__author__ = 'Ville'

""" Täydennä tähän koodipohjaan kaikki kohdat, joissa lukee TODO tai pass
 TIE-02100 Johdatus ohjelmointiin S2015
 TODO: oma_opiskelijanumero, oma_sähköpostiosoite
 TODO: Ohjelmointitehtävä T2
 TODO: Lyhyt selitys ohjelman toiminnasta
 """


def tankkaa(tankin_koko, lisä_bensa, bensa):
    """ TODO: funktion toiminnan kuvaus

    Parametrien on oltava alla esitetyssä järjestyksessä, muutoin
    ohjelma ei tule läpäisemään automaattisia testejä. Funktio ei saa tulostaa
    näytölle mitään, eikä se saa lukea syötteitä näppäimistöltä.

    Parametrit:
    TODO: tankin koko
    TODO: tankattavaksi haluttu bensamäärä
    TODO: tankissa tällä hetkellä oleva bensamäärä

    Paluuarvo:
    TODO: Tankissa tankkauksen jälkeen oleva bensan määrä desimaalilukuna (float)
    """
    bensa += lisä_bensa
    if bensa > tankin_koko:
        bensa = tankin_koko
    return  bensa


def aja(x = 1, y = 1, komento = "", tankki = 0, kulutus = 1, kartan_koko = 0):
    """ TODO: funktion toiminnan kuvaus

    Sekä parametrien että paluuarvojen on oltava alla esitetyssä järjestyksessä,
    muutoin ohjelma ei tule läpäisemään automaattisia testejä. Funktio ei saa
    tulostaa näytölle mitään, eikä se saa lukea syötteitä näppäimistöltä.

    Parametrit:
    TODO: Lähtöpisteen x-koordinaatti
    TODO: Lähtöpisteen y-koordinaatti
    TODO: Suunta johon halutaan mennä (str)
    TODO: Tankissa lähtöhetkellä oleva bensan määrä
    TODO: Auton kulutus per kilometri
    TODO: Kartan koko

    Paluuarvot:
    TODO: Ajomatkan saavutetun päätepisteen x-koordinaatti (int)
    TODO: Ajomatkan saavutetun päätepisteen y-koordinaatti (int)
    TODO: Ajomatkan jälkeen tankissa jäljellä oleva bensan määrä (float)
    """

    if tankki == 0:
        return x, y, tankki
    elif tankki - kulutus < 0:
        return x, y, tankki
    elif (komento == "L"):
        if  x - 1 < 1:
            return x, y, tankki
        else:
            return (x - 1), y, (tankki - kulutus)
    elif komento == "E":
        if y -1 < 1:
            return x, y, tankki
        else:
            return x, (y - 1), (tankki - kulutus)
    elif komento == "P":
        if y + 1 > kartan_koko:
            return x, y, tankki
        else:
            return x, (y + 1), (tankki - kulutus)
    elif komento == "I":
        if x + 1 > kartan_koko:
            return x, y, tankki
        else:
            return (x + 1), y, (tankki - kulutus)
#
def muotoile_auton_rivi(x = 1, kartan_koko = 4):
    #kartan_koko -= 2
    viiva = " ." * (x - 1)
    viiva += " A "
    viiva += ". " * (kartan_koko - x)
    return viiva
#
def tulosta_kartta(x, y, kartan_koko):
    """ TODO: funktion toiminnan kuvaus

    Parametrien on oltava alla esitetyssä järjestyksessä, muutoin
    ohjelma ei tule läpäisemään automaattisia testejä. Funktio ei saa lukea
    syötteitä näppäimistöltä. Funktion tulee printata kartta tehtävänannossa
    määritellyllä tavalla eikä se palauta mitään.

    Parametrit:
    TODO: Auton sijainnin x-koordinaatti
    TODO: Auton sijainnin y-koordinaatti
    TODO: Kartan koko
    """
    pisteet = "." * (kartan_koko -3)
    i = kartan_koko
    while i >= 0:

        if i == 0:
            print( "  +" + " -" * (kartan_koko) )
        elif i == y:
            print( "{} |".format(i % 10) + muotoile_auton_rivi( x, kartan_koko) )
        else:
            print( "{} |".format(i % 10) + " ." * (kartan_koko ))
        #for i in range( kartan_koko ):
            #pass

        i -= 1

    pohja = "   "
    for i in range(kartan_koko):
        pohja += " {}".format( (i + 1) % 10 )
    print(pohja)

#
def lue_luku(kehote, virheilmoitus="Virhe: vääräntyyppinen syöte."):
    """ Lukee käyttäjältä syötettä, kunnes käyttäjän antama syöte on
    positiivinen luku. Sinun ei tarvitse muokata tätä funktiota eikä ymmärtää
    sen toimintaa, mutta voit halutessasi tutustua siihen.
    """

    try:
        luku = float(input(kehote))
        if luku <= 0:
            raise ValueError
        else:
            return luku
    except ValueError:
        print(virheilmoitus)
        return lue_luku(kehote, virheilmoitus)


def main():

    x = 1
    y = 1
    kartan_koko = int(lue_luku("Syötä kartan koko: "))
    tankin_koko = lue_luku("Syötä tankin koko: ")
    kulutus = lue_luku("Syötä auton kulutus per kilometri: ")
    bensaa = tankin_koko #tankissa olevan bensan määrä

    while True:

        print("Koordinaatit x={}, y={}, tankissa on {:.1f}"
              " litraa polttoainetta.".format(x, y, bensaa))

        komento = input("Anna komento T/P/I/E/L/K/Q: ")
        komento = komento.upper()

        if komento == "T":
            tankataan = lue_luku("Montako litraa tankataan: ")
            tankataan = float(tankataan)
            bensaa = tankkaa(tankin_koko, tankataan,bensaa)

        elif komento in "PIEL" and len(komento) == 1:
            x, y, bensaa = aja(x, y, komento, bensaa, kulutus, kartan_koko)

        elif komento == "K":
            tulosta_kartta(x, y, kartan_koko)

        elif komento == "Q":
            return

        else:
            print("Virhe: tuntematon komento")

main()
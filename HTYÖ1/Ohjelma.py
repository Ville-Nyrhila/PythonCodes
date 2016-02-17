__author__ = 'Ville'

def oltava_pos_kokLuku():
    ''' Tulostaa, että mittausten määräksi on annettu väärä luku.
    '''
    print("Virhe: mittausten lukumäärän tulee olla positiivinen kokonaisluku.")

def ei_sopivat():
    ''' Tulostaa, että olot eivät ole sopivat.
    '''
    print("Olosuhteet eivät ole seeprakalalle sopivat.")

def kysy_mittaukset():
    ''' Kysytään, montako mittausta tehdään.

    :return 0: Palautetaan 0, jos määräksi annetaan kielletty luku.
    :return rivi: Palautetaan lukumäärä, jos luku on sallittu.
    '''
    rivi = int(input("Syötä mittausten lukumäärä: "))
    if (rivi <= 0):
        oltava_pos_kokLuku()
        return 0
    return  rivi

def kysy_mittausTulos(luku, vanha):
    ''' Funktio, jolla kysytään mittaustulokset, ja tarkistetaan,
    ovatko ne sallitulla alueella.

    :param luku: kuvastaa, monesko kerta for-loopissa on meneillään.
    :param vanha: edellisessä mittauksessa saatu luku
    :return 0: palautetaan tulokseksi 0, jos tulos oli virheelline
    :return tulos: Jos tulos oli kunnossa, palautetaan se kutsuvaan funktioon.
    '''
    tulos = input("Syötä {}. mittaustulos: ".format(luku + 1))
    tulos = float(tulos)
    if(tulos > 8.0):
        return 0
    elif(tulos < 6.0):
        return 0
    elif (abs(tulos - vanha) > 1.0):
        return 0
    else:
        return tulos

def main():
    ''' Pääfunktio. Kutsuu funktion kysy_mittaukset(), jolla kysyy
    mittauksien määrän, sitten kysyy jokaisen mittauskerran
    tuloksen.

    Jos olosuhteet ovat sopivat, ohjelma kertoo sen ja antaa
    mittausten keskiarvon.
    Jos ei, sopimattomuudesta kerrotaan ja ohjelman suoritus
    päättyy.
    '''

    ka = 0.0
    luku = 0.0
    vanha = 7.0

    #lippu, jolla katso, onko tapahtunut virhe.
    virhe = False

    määrä = kysy_mittaukset()
    #Jos määrä oli väärä, hypätään ohjelman loppuun.
    if (määrä != 0):

        #Tarkastellaan annettu määrä pH-testejä.
        for i in range(määrä):

            luku = kysy_mittausTulos(i,vanha)

            if (luku == 0):
                ''' Jos on tullut väärä luku, ilmoitetaan,
                että olot ovat sopimattomat, asetetaan
                virhelippu pystyyn, lopetetaan silmukka.

                Ohjelma siirtyy loppuun.
                '''
                ei_sopivat()
                virhe = True
                break
            ka = ka + luku
            vanha = luku

        if ( virhe == False ):
            ''' Jos virhettä ei ole tullut, lasketaan keskiarvo.
            Ilmoitetaan kaiken olevan kunnossa ja ilmoitetaan keskiarvo
            kahden desimaalin tarkkuudella.
            '''
            ka = ka / määrä
            print("Olosuhteet ovat seeprakalalle sopivat. Mittausten keskiarvo on %.2f." % ka)

main()
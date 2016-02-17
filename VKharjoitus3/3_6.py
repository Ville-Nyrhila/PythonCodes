__author__ = 'Ville'

def lue_syöte(kys):
    ''' Ottaa syötteen ja tarkistaa, onko se nollaa suurempi

    :param kys: Merkkijono jolla kysytään käyttäjältä haluttua tietoa
    :return: Palauttaa kysytyn nollaa suuremman kokonaisluvun
    '''
    luku = -1
    while luku <= 0:
        luku = input(kys)
        luku = int(luku)
    return luku

def tulosta_ruutu(l,k,m):
    ''' Tulostaa parametrien mukaisesti ruudun

    :param l: ruudun leveys
    :param k: ruudun korkeus
    :param m: merkki, jolla ruudukko ruutu piirretään
    '''
    for i in range(k):
        print(m * l)

def main():
    ''' Pääfunktio, kysyy leveyden, korkeuden ja piirrosmerkin
        ja muodostaa näiden perusteella ruudun
    '''
    #Otetaan leveys
    leveys = lue_syöte("Syötä ruudun leveys: ")

    #Otetaan korkeus
    korkeus = lue_syöte("Syötä ruudun korkeus: ")

    #Otetaan piirtämiseen käytettävä merkki
    merkki = input("Syötä tulostusmerkki: ")

    #Piirretään ruutu edellä otetuilla merkeillä
    tulosta_ruutu(leveys, korkeus, merkki)

main()

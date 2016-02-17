__author__ = 'Ville'

def onko_numero(sana = ""):
    try:
        luku = int(sana)
        return True
    except ValueError:
        #Virhe
        return False
#
def check_file( nimi = ""):
    try:
        filu = open( nimi )
        filu.close()
        return True
    except FileNotFoundError:
        return False
#
def take_file( file = "" ):
    kadut = {}
    kaupungit = {}
    osat = []

    try:
        tiedosto = open(file, 'r', encoding="utf-8")

        for rivi in tiedosto:
            rivi = rivi.rstrip()
            osat = rivi.split(' ')
            if onko_numero(osat[0]):
                kaupungit[ osat[0] ] = osat[1]
            elif onko_numero(osat[1]):
                kadut[ osat[0] ] = osat[1]

        tiedosto.close()

        return kadut, kaupungit
    except FileNotFoundError:
        return 0
#
def kysymys(kadut = {}, kaupungit = {}):
    osoite = input("Syötä osoite: ")
    if osoite in kadut:

        if kadut[osoite] in kaupungit:
            print(osoite + " " + kadut[osoite] + " " + kaupungit[kadut[osoite]])
        else:
            print(osoite + " " + kadut[osoite] + " postitoimipaikka puuttuu tietojärjestelmästä" )
    else:
        print("Osoite puuttuu tietojärjestelmästä.")
#
def main():
    file = input("Syötä tiedoston nimi: ")
    if check_file(file):
        kadut, kaupungit = take_file( file )
        kysymys(kadut, kaupungit)
#
main()
__author__ = 'Ville'

def file_to_dict():
    nimi = input("Syötä tiedoston nimi: ")
    try:
        tiedosto = open(nimi, 'r', encoding="utf-8")
    except FileNotFoundError:
        print("Tiedoston lukeminen epäonnistui.")
        return 0
    except PermissionError:
        print("Tiedoston lukeminen epäonnistui.")
        return 0

    sanakirja = {}
    palat = []
    luku = 0

    for rivi in tiedosto:
        rivi = rivi.rstrip()
        if ":" not in rivi:
            print("Tiedoston rivi ei sisältänyt kahta kaksoispisteellä erotettua kenttää.")
            return 0

        palat = rivi.split(':')
        try:
            luku = int( palat[1] )
            sanakirja[palat[0]] = luku
        except ValueError:
            print("Tiedoston rivin viimeisenä kenttänä ei ollut numero.")
            return 0

    return sanakirja
#
def kysy_laji(sanakirja = {}):
    ruoka = ""
    while True:
        ruoka = input("Mitä söit: ")
        if ruoka not in sanakirja:
            print("Syötit tuntemattoman ravintoaineen nimen.")
            return 0
        else:
            return ruoka
#
def kysy_ja_laske(sanakirja = {}, sana = ""):
    while True:
        try:
            eaten = input("Kuinka paljon söit (grammoja): ")
            eaten = int(eaten)
            break
        except ValueError:
            pass
    luku = eaten * sanakirja[sana]
    luku = luku/100
    print("Sait energiaa: {:.1f}".format( luku ) + " kJ")
#
def main():
    sanakirja = file_to_dict()
    if sanakirja != 0:
        ruoka = kysy_laji(sanakirja)
        if ruoka != 0:
            kysy_ja_laske( sanakirja, ruoka )
#
main()
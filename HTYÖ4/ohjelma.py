__author__ = 'Ville'

def lue_nimet():
    tidNimi = input("Anna nimitiedoston nimi: ")

    sanakirja = {}
    try:
        filu = open(tidNimi, 'r', encoding="utf-8")
        for rivi in filu:
            rivi = rivi.rstrip()
            osat = rivi.split(":")

            if len(osat) != 2:
                print("Virhe: nimitiedoston rivien oltava muotoa nimi:kilpailunumero.")
                filu.close()
                return None

            nimi = osat[0]
            nro = osat[1]

            if nro.isdigit() == False or nimi.isdigit() == True:
                print("Virhe: nimitiedoston rivien oltava muotoa nimi:kilpailunumero.")
                filu.close()
                return None
            if nro not in sanakirja:
                sanakirja[ nro ] = nimi
            else:
                print("Virhe: tiedostossa samoja kilpailunumeroita.")
                filu.close()
                return None

    except Exception:
        print("Virhe: tiedostoa {} ei voida lukea.".format(tidNimi))
        return None

    filu.close()
    return sanakirja
#
def lue_pisteet(nimet = {}):
    tidNimi = input("Anna pistetiedoston nimi: ")

    numeroview = nimet.keys()

    sanakirja = {}
    try:
        filu = open(tidNimi, 'r', encoding="utf-8")
        for rivi in filu:
            rivi = rivi.rstrip()
            osat = rivi.split(":")

            if len(osat) != 2:
                print("Virhe: pistetiedoston rivien pitää olla muotoa kilpailunumero:pisteet.")
                filu.close()
                return None

            nro = osat[0]
            pisteet = osat[1]

            if pisteet == "" or nro == "":
                print("Virhe: pistetiedoston rivien pitää olla muotoa kilpailunumero:pisteet.")
                filu.close()
                return None
            if pisteet.isdigit() == False:
                print("Virhe: pisteiden on oltava kokonaislukuja.")
                filu.close()
                return None
            if float(pisteet) % 1 != 0:
                print("Virhe: pisteiden on oltava kokonaislukuja.")
                filu.close()
                return None
            if nro.isdigit() == False:
                if float(nro) % 1 != 0:
                    print("Virhe: pistetiedoston rivien pitää olla muotoa kilpailunumero:pisteet.")
                    filu.close()
                    return None
            if nro not in numeroview:
                print("Virhe: tiedostossa tuntematon kilpailunumero.")
                filu.close()
                return None
            if nro not in sanakirja:
                sanakirja[ nro ] = int(pisteet)
            else:
                sanakirja[ nro ] += int(pisteet)

    except Exception:
        print("Virhe: tiedostoa {} ei voida lukea.".format(tidNimi))
        return None

    filu.close()
    return sanakirja
#
def main():
    nimet = lue_nimet()
    if nimet != None:
        pisteet = lue_pisteet(nimet)

        if pisteet != None:
            print("Seitsenottelun tulokset ovat:")
            luku = 1
            for rivi in sorted(pisteet, reverse=True, key=(lambda rivi: pisteet[rivi]) ):
                print("{}. ".format(luku) + "{} ".format(nimet[rivi]) + "{}".format(pisteet[rivi]))
                luku += 1
#
main()
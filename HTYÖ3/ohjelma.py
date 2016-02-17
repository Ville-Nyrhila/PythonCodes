__author__ = 'Ville'

def aseta_kirjain_viivoihin(mysteeri = "", viivat = "", merkki = ""):
    indeksi = 0
    while True:
        indeksi = mysteeri.find(merkki, indeksi)
        #viivat = viivat[:-indeksi] + mysteeri[indeksi]
        viivat = viivat[:indeksi] + mysteeri[indeksi] + viivat[(indeksi + 1):]
        indeksi += 1
        if mysteeri.find(merkki, indeksi) == -1:
            break

    return viivat
#
def luo_viivat(mysteeri = ""):
    return "_" * len(mysteeri)
#
def ota_arvuuteltava_sana():
    sana = input("Syötä arvuuteltava sana: ")
    print("Putsataan näyttö...")
    for i in range(0, 10):
        print()
    sana = sana.upper()
    return sana
#
def ota_arvaus():
    kirjain = input("Arvaa kirjain: ")
    kirjain = kirjain.upper()
    return kirjain
#
def main():

    mysteeri = ota_arvuuteltava_sana()

    viivat = luo_viivat(mysteeri)
    sanakirja = {}
    kerrat = 0

    print("Peli alkakoon! Saat arvata 10 kirjainta. Mikä sana on kyseessä?".format(len(mysteeri)))
    while True:
        print(viivat)
        kirjain = ota_arvaus()
        kerrat += 1


        if len(kirjain) != 1:
            print("Virhe: syötä yksi kirjain.")
        else:
            if kirjain in sanakirja:
                print("Hölmö arvaus, {} on jo arvattu.".format(kirjain))
            else:
                sanakirja[kirjain] = True
                if kirjain in mysteeri:
                    viivat = aseta_kirjain_viivoihin(mysteeri, viivat, kirjain)
                    #print(viivat)

                else:
                    #print(viivat)
                    pass
        if viivat == mysteeri:
            print(viivat)
            print("Hyvä! Arvasit koko sanan!")
            break
        if kerrat == 10:
            print(viivat)
            print("Arvauskerrat loppuivat kesken. Sana olisi ollut {}".format(mysteeri))
            break
#

main()
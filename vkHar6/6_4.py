__author__ = 'Ville'

def korjaa_pala(sana = ""):
    eka = sana[0].upper()
    toka = sana[1:]
    uus = ""
    for merkki in toka:
        uus += merkki.lower()
    eka += uus
    return eka
#
def tee_muutos(lause = ""):
    osat = lause.split()
    palaute = ""
    for sana in osat:
        palaute += korjaa_pala(sana)
        palaute += " "
    palaute = palaute[:(len(palaute)-1)]
    return palaute
#
def main():
    sana = input("Syötä merkkijono: ")
    print("Muutettuna: ", tee_muutos(sana))


main()
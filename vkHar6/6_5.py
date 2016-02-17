__author__ = 'Ville'
def etsi_abba(virke = ""):
    if virke.find("abba") != -1:
        return  1 + \
                etsi_abba(virke[(virke.find("abba") + 1):])
    else:
        return 0
#
def laske_abba(virke = ""):
    palaute = etsi_abba(virke)
    return palaute
#
def main():
    virke = input("Syötä merkkijono: ")
    print("Merkkijono {} sisältää {} merkkijonoa abba".format(virke, laske_abba(virke)))


main()
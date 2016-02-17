__author__ = 'Ville'

def tee_lyhenne(nimi = ""):
    osat = nimi.split()
    lyhenne = ""
    for pala in osat:
        lyhenne += pala[0].upper()
    return lyhenne
#
def main():
    nimi = input("Syötä nimi, josta tehdään akronyymi: ")
    print("Akronyymi on: ", tee_lyhenne(nimi))


main()
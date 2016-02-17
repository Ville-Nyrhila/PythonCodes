__author__ = 'Ville'

def read_file():
    nimi = input("Syötä tiedoston nimi: ")
    tiedosto = open(nimi, "r", encoding="utf-8")
    i = 0
    for rivi in tiedosto:
        i += 1
        rivi = rivi.rstrip()
        print("{}".format(i),rivi)
    tiedosto.close()
#
def main():
    try:
        read_file()
    except Exception:
        main()
#
main()
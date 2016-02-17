__author__ = 'Ville'

def käännä_nimi(nimi = ""):
    nimi = nimi.split(',')
    for osa in nimi:
        osa = osa.strip()
    nimi = nimi[1] + " " + nimi[0]
    return nimi
#
def main():
    nimi = input("Syötä nimi takaperoisessa järjestyksessä: ")
    print("Nimi oikein päin:", käännä_nimi(nimi))


main()
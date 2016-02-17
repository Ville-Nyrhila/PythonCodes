__author__ = 'Ville'

def ota_luku(Prompt = ""):
    try:
        ote = input(Prompt)
        ote = int(ote)
        if ote < 0:
            return ota_luku(Prompt)
        return ote
    except ValueError:
        return ota_luku(Prompt)
#
def main():
    leveys = ota_luku("Syötä ruudun leveys: ")
    korkeus = ota_luku("Syötä ruudun korkeus: ")
    merkki = input("Syötä tulostusmerkki: ")
    print()
    for i in range(korkeus):
        print(leveys*merkki)
#
main()
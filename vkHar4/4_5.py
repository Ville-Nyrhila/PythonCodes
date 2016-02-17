__author__ = 'Ville'

def tulosta_ruutu(leveys, korkeus, reunamerkki = "#", sisämerkki = " "):
    print(leveys * reunamerkki)
    alue = korkeus - 2
    for i in range(alue):
        print(reunamerkki + sisämerkki * (leveys - 2) + reunamerkki)
    print(leveys * reunamerkki)
    print()

def main():
    tulosta_ruutu(5, 4)
    tulosta_ruutu(3, 8, "*")
    tulosta_ruutu(5, 4, "O", "o")
    tulosta_ruutu(sisämerkki=".", reunamerkki="O", korkeus=4, leveys=6)

main()
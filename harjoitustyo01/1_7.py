__author__ = 'Ville'

def main():
    p1 = input("Pelaaja 1, syötä valintasi (K/P/S): ")
    p2 = input("Pelaaja 2, syötä valintasi (K/P/S): ")

    if(p1 == p2):
        tasa()
    else:
        if (p1 == "K" and p2 == "S"):
            voitto(1)
        elif (p1 == "K" and p2 == "P"):
            voitto(2)
        elif (p1 == "P" and p2 == "K"):
            voitto(1)
        elif (p1 == "P" and p2 == "S"):
            voitto(2)
        elif (p1 == "S" and p2 == "P"):
            voitto(1)
        elif (p1 == "S" and p2 == "K"):
            voitto(2)

def tasa():
    print("Tuli tasapeli.")

def voitto(pla):
    print("Pelaaja {} voitti!".format(pla))

main()
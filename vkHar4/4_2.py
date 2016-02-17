__author__ = 'Ville'

def kertoma(ännä):
    tulos = ännä
    ännä -= 1
    while(ännä > 0):
        tulos *= ännä
        ännä -= 1
    return tulos

def paree_kertoma(ännä, pee):
    tulos = ännä
    ero = ännä - pee
    ännä -= 1
    while(ännä > ero):
        tulos *= ännä
        ännä -= 1
    return tulos

def yhtälö(ännä, pee):
    aaa = paree_kertoma(ännä, pee)
    #print(aaa)
    bbb = kertoma(pee)
    #print(bbb)
    tulos = aaa / bbb
    #print(tulos)
    return tulos

def kysy_pallot():
    lottopallot = input("Syötä lottopallojen kokonaismäärä: ")
    lottopallot = int(lottopallot)
    arvottavat = input("Syötä arvottavien pallojen määrä: ")
    arvottavat = int(arvottavat)

    return lottopallot, arvottavat

def main():
    pallot, arvot = kysy_pallot()
    tn = yhtälö(pallot, arvot)
    #tn = 1/tn
    print("Kun pelataan yksi rivi, todennäköisyys saada", arvot, "oikein on 1/%.0f" % tn)

main()

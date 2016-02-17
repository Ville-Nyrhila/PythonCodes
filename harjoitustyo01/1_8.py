__author__ = 'Ville'

def main():
    hinta = input("Ostosten hinta: ")
    hinta = int(hinta)
    maksu = input("Maksettu rahasumma: ")
    maksu = int(maksu)

    vaihto = maksu - hinta

    hintaalapi(vaihto)

#
def hintaalapi(vaihto):
    if (vaihto != 0):
        print("Anna vaihtorahaa:")
        kympit = vaihto // 10
        if(kympit != 0):
            print("{}".format(kympit) + " kymppiä")
        vaihto -= 10*kympit
        vitoset = vaihto // 5
        if(vitoset != 0):
            print("{}".format(vitoset) + " vitosta")
        vaihto -= 5*vitoset
        kakoset = vaihto // 2
        if (kakoset != 0):
            print("{}".format(kakoset) + " kaksieuroista")
        vaihto -= 2*kakoset
        if (vaihto != 0):
            print("{}".format(vaihto) + " euroa")
    else:
        print("Ei vaihtorahaa")
#
main()
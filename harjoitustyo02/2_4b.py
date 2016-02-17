__author__ = 'Ville'

def main():
    kerrat = input("Kuinka monta Fibonaccin lukua haluat: ")
    kerrat = int(kerrat)
    maxi = 1000 * kerrat
    tulos = 0
    uus = 1
    eka = 0
    toka = 0
    for i in range(1,102):
        print("{}.".format(i), "{}".format(uus))
        toka = eka
        eka = uus
        uus = eka + toka
        if (i == kerrat):
            break


main()
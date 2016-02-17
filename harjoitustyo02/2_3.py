__author__ = 'Ville'

def main():
    kerrat = input("Kuinka monta Fibonaccin lukua haluat: ")
    kerrat = int(kerrat)
    kerrat += 1
    uus = 1
    eka = 0
    toka = 0
    for i in range(1,kerrat):
        print("{}.".format(i), "{}".format(uus))
        '''if(i % 2 == 0):
            toka = eka + toka
        else:
            eka = eka + toka'''
        toka = eka
        eka = uus
        uus = eka + toka
#
main()
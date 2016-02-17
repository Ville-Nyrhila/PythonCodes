__author__ = 'Ville'

def main():
    luku = input("Syötä luku: ")
    luku = int(luku)
    tulos = 0
    i = 1
    while(True):
        tulos = luku * i
        print("%i" % i,"*","%i" % luku,"= {}".format(tulos))
        i += 1
        if (tulos > 100):
            break

main()
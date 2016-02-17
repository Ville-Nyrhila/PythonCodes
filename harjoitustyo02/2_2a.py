__author__ = 'Ville'

def main():
    luku = input("Syötä luku: ")
    luku = int(luku)
    for i in range(1,11):
        print("%i" % i,"*","%i" % luku,"= {}".format(luku * i))

main()
__author__ = 'Ville'
import math


def laske_S(a, b, c):
    return ((a + b + c)/2)

def laske_Ala(a, b, c):
    s = laske_S(a, b, c)
    return math.sqrt(s*(s-a)*(s-b)*(s-c))

def main():
    rivi = input("Syötä ensimmäinen sivun pituus: ")
    a = float(rivi)
    rivi = input("Syötä toinen sivun pituus: ")
    b = float(rivi)
    rivi = input("Syötä kolmas sivun pituus: ")
    c = float(rivi)

    print("Kolmion pinta-ala on %.1f" % laske_Ala(a,b,c))


main()
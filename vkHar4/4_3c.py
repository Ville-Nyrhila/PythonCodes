__author__ = 'Ville'
import math

def take_input(prompt):
    rivi = 0.0
    while rivi <= 0:
        rivi = input(prompt)
        rivi = float(rivi)
    return rivi

def neliö():
    sivu = take_input("Syötä neliön sivun pituus: ")

    print("Ympärysmitta on %.2f" % (sivu * 4))
    print("Pinta-ala on %.2f" % (sivu**2))

def suorakaide():
    lev = take_input("Syötä suorakaiteen sivun 1 pituus: ")
    kork = take_input("Syötä suorakaiteen sivun 2 pituus: ")

    print("Ympärysmitta on %.2f" % (lev * 2 + kork * 2))
    print("Pinta-ala on %.2f" % (lev * kork))

def ympyrä():
    säde = take_input("Syötä ympyrän säde: ")

    print("Ympärysmitta on %.2f" % (2 * säde * math.pi))
    print("Pinta-ala on %.2f" % ((säde ** 2)* math.pi))

def valikko():
    while True:
        vastaus = input("Syötä kuvion alkukirjain, q lopettaa (n/s/y/q): ")
        if vastaus == "n":
            # Tässä käsitellaan neliö
            neliö()
        elif vastaus == "s":
            # Tässä käsitellään suorakaide
            suorakaide()
        elif vastaus == "y":
            # Tässä käsitellään ympyrä
            ympyrä()
        elif vastaus == "q":
            return
        else:
            print("Virheellinen syöte, yritä uudelleen!")
        print()  # Tyhjä rivi, että ohjelman tulostetta on helpompi lukea


def main():
    valikko()
    print("Näkemiin!")


main()
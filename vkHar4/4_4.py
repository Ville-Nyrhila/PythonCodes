__author__ = 'Ville'

def take_input(prompt):
    rivi = 0.0
    while rivi <= 0:
        rivi = input(prompt)
        rivi = float(rivi)
    return rivi

def pinta_ala(xx, yy = None):
    if yy == None:
        yy = xx

    return xx * yy

def main():
    print("Neliön pinta-ala on {:.1f}".format(pinta_ala(3)))
    print("Suorakaiteen pinta-ala on {:.1f}".format(pinta_ala(4,3)))


main()
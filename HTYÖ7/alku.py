__author__ = 'Ville'

import tkinter as tk
import ristinolla

class alkuRuutu():

    def __init__(self):

        self.__root = tk.Tk()
        self.__root.title( "Ristinollapeli" )

        self.__title = tk.Label( self.__root, text="Ristinollapeli")
        self.__title.pack()

        self.__ohjeLabel = tk.Label( self.__root, text="\nLaita tähän haluamasi ruutujen määrä.\nSe voi olla jokin luku 3-10.")
        self.__ohjeLabel.pack()

        self.__entry = tk.Entry( self.__root )
        self.__entry.bind( "<Return>", self.enterBtn)
        self.__entry.pack()

        #
        self.__vaikeusLabel = tk.Label( self.__root, text="\nLaita alle haluamasi vaikeustaso." \
                                                          + "\nJos et laita mitään, tulee voiton ehdoksi kolme peräkkäistä ruutua." \
                                        + "\nJos laitat suuremman luvun kuin ruutujen määrä, \nlaitetaan ehdoksi ruutujen määrä." \
                                         + "\nMinimi on joka tapauksessa kolme.")
        self.__vaikeusLabel.pack()
        self.__vaikeusEntry = tk.Entry( self.__root )
        self.__vaikeusEntry.bind( "<Return>", self.enterBtn )
        self.__vaikeusEntry.pack()
        #

        self.__button = tk.Button( self.__root, text="Aloita peli", command=self.buttonPress )
        self.__button.pack()

        self.__root.mainloop()

    def enterBtn(self, event):
        self.buttonPress()
    #
    def buttonPress(self):
        teksti = self.__entry.get()
        vaikeus = self.__vaikeusEntry.get()

        try:
            vaikeus = int( vaikeus )

            if vaikeus < 3:
                vaikeus = 3

        except ValueError:
            vaikeus = 3

        try:
            teksti = int(teksti)

            if vaikeus > teksti:
                vaikeus = teksti - 1

            if 11 > teksti > 2:
                ristinolla.Ristinollaruutu( teksti, vaikeus )

        except ValueError:
            pass
#
def main():
    alkuRuutu()

main()
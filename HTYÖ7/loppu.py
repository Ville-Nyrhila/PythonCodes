__author__ = 'Ville'

import tkinter as tk

class LoppuRuutu():

    def __init__(self, Pelaaja = "X", Tasapeli = False, Lopetti = False, Emo = None ):

        self.__root = tk.Tk()

        teksti = ""

        if Lopetti:
            teksti = "Keskeytit pelin.\n\nPeli suljetaan."
            self.__emo = Emo
        elif Tasapeli:
            teksti = "Peli päättyi tasapeliin.\n\nTs. kumpikin hävisi.\n\nMuhahahahaa!"
        else:
            # Pelaaja voitti
            teksti = "{} voitti tämän pelin.".format( Pelaaja )

        self.__laabeli = tk.Label( self.__root, text=teksti )
        self.__laabeli.pack()

        self.__button = tk.Button( self.__root, text="Ok!", command=self.sulje )
        self.__button.pack()

        self.__root.mainloop()

    def sulje(self):

        self.__root.destroy()
        if self.__emo != None:
            self.__emo.destroy()



            #LoppuRuutu( Lopetti=True )
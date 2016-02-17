__author__ = 'Ville'

import tkinter as tk
import random
import  loppu

# Modeli ristinollan sääntöihin.
class Model():

    def __init__(self, määrä = 3, Vaikeus = None):

        self.__ruksinVuoro = bool( random.getrandbits(1) )

        self.__tasapeli = False

        self.__vaikeus = Vaikeus
        if Vaikeus == None:
            self.__vaikeus = 3

        self.__taulu = []

        for i in range( määrä ):
            tmp = []
            for k in range( määrä ):
                tmp.append(".")
            self.__taulu.append( tmp )
    #
    def vuoro(self):
        return self.__ruksinVuoro
    #
    def tarkista_paikka(self, X = 0, Y = 0):
        merkki = ""
        if self.__ruksinVuoro:
            merkki = "X"
        else:
            merkki = "O"

        if self.__taulu[Y][X] == ".":
            self.__taulu[Y][X] = merkki

            self.vaihda_vuoro()

            return True
        else:
            return False
    #
    def vaihda_vuoro(self):
        if self.__ruksinVuoro:
            self.__ruksinVuoro = False
        else:
            self.__ruksinVuoro = True
    #
    def __str__(self):
        palaute = ""
        for pala in self.__taulu:
            for osa in pala:
                palaute += osa
            palaute += "\n"

        return palaute
    #
    def pystyt(self):

        merkit = "XO"
        merkki = ""
        lippu = False
        counter = 0

        for i in range( len( self.__taulu)):
            for k in range( len( self.__taulu)):

                if self.__taulu[k][i] in merkit:

                    if not lippu:
                        merkki = self.__taulu[k][i]
                        lippu = True
                    #
                    if self.__taulu[k][i] == merkki:
                        counter += 1
                    else:
                        counter = 0
                        lippu = False
                else:
                    counter = 0
                    lippu = False

                if counter >= self.__vaikeus:
                    return True
    #
    def vaaka(self):

        merkit = "XO"
        merkki = ""
        lippu = False

        counter = 0
        for rivi in self.__taulu:

            merkki = ""
            for pala in rivi:

                if pala in merkit:

                    if not lippu:
                        merkki = pala
                        lippu = True

                    if pala == merkki:
                        counter += 1
                    else:
                        lippu = False
                        counter = 0
                else:
                    counter = 0
                    lippu = False


                if counter >= self.__vaikeus:
                    return True
    #
    def vinot_vasen(self):

        merkit = "XO"
        merkki = ""
        lippu = False
        counter = 0

        alkux = len( self.__taulu) - 1
        alkuy = 0

        muutosX = 0
        muutosY = 0

        for mn in range ( 2 * len( self.__taulu) ):

            x = alkux - muutosX
            y = alkuy

            muutosX += 1
            if x < 0:
                x = 0
                y = alkuy + muutosY
                muutosY += 1

            while x < len( self.__taulu) and y < len( self.__taulu):

                #print( x, y )
                if self.__taulu[y][x] in merkit:

                    if not lippu:
                        merkki = self.__taulu[y][x]
                        lippu = True
                    #
                    if self.__taulu[y][x] == merkki:
                        counter += 1
                    else:
                        counter = 0
                        lippu = False
                else:
                    counter = 0
                    lippu = False
                #
                #if self.__taulu[y][x] != '.':
                    #print( counter, self.__taulu[y][x], x, y )

                y += 1
                x += 1

                # While y loppuu.
                if counter >= self.__vaikeus:
                    return True
            # While x loppuu.

        # For loppuu.

        return False
    #
    def vinot_oikea(self):

        merkit = "XO"
        merkki = ""
        lippu = False
        counter = 0

        alkux = 0
        alkuy = 0#len( self.__taulu) - 1

        muutosX = 0
        muutosY = 0

        for mn in range ( 2 * len( self.__taulu) ):

            y = alkuy
            x = alkux + muutosX

            muutosX += 1
            if x >= len( self.__taulu):
                x = len( self.__taulu ) - 1
                y = alkuy + muutosY
                muutosY += 1

            while x >= 0 and y < len( self.__taulu):

                #print( "Kierroksen koordinaatit:", x, y )
                if self.__taulu[y][x] in merkit:

                    if not lippu:
                        merkki = self.__taulu[y][x]
                        lippu = True
                    #
                    if self.__taulu[y][x] == merkki:
                        counter += 1
                    else:
                        counter = 0
                        lippu = False
                else:
                    counter = 0
                    lippu = False
                #
                #if self.__taulu[y][x] != '.':
                    #print( counter, self.__taulu[y][x], x, y )

                y += 1
                x -= 1

                if counter >= self.__vaikeus:
                    return True
            # While loppuu.

        # For loppuu.

        return False

        return False
    #
    def kaikki_taynna(self):

        for rivi in self.__taulu:
            for merkki in rivi:
                if merkki == ".":
                    return False

        self.__tasapeli = True
        return True
    #
    def loppuiko(self):

        # Vaakarivit
        if self.vaaka():
            return True

        # Pystyrivit
        if self.pystyt():
            return True

        # Vinot rivit

        # Vasemmalta alaviistoon oikealle.
        if self.vinot_vasen():
            return True

        # Oikealta alaviistoon vasemmalle.
        if self.vinot_oikea():
            return True

        if self.kaikki_taynna():
            return True

        return False
#
    def oliko_tasapeli(self):
        return self.__tasapeli
    #
    def kenenVuoro(self):
        if self.__ruksinVuoro:
            return "X"
        else:
            return "O"
#
#
class Ristinollaruutu():

    def __init__(self, määrä = 3, Vaikeus = None ):

        self.__model = Model( määrä, Vaikeus )

        self.__ruksin_Vuoro = self.__model.vuoro()

        self.__root = tk.Tk()

        self.__root.title( "Ristinollapeli" )

        self.__kuvat = []

        self.__lf = tk.Frame( self.__root )
        self.__lf.pack()
        self.__rf = tk.Frame( self.__root )
        self.__rf.pack()

        #
        self.__button = tk.Button( self.__lf, text="Lopeta peli.", command=self.lopetaBtn)
        self.__button.pack( side=tk.LEFT )


        self.__tilanneLabel = tk.Label( self.__lf, text="Vuorossa on {}".format( self.__model.kenenVuoro() ) )
        self.__tilanneLabel.pack( side=tk.LEFT )
        #

        self.__tyhja = tk.PhotoImage( master=self.__root, file="tyhja.gif" )
        self.__rengas = tk.PhotoImage( master=self.__root, file="rengas.gif" )
        self.__raksi = tk.PhotoImage( master=self.__root, file="raksi.gif" )

        #self.__raksi = tk.Image( file="raksi.gif" )
        #self.__raksi.

        counter = 0

        # Vaakarivit
        for i in range(määrä):

            # Sarakkeet
            for k in range(määrä):
                #self.__kuvat.append( tk.Label( self.__root, image=self.__tyhja, text="{} {}".format(k, i) ) )
                self.__kuvat.append( tk.Label( self.__rf, image=self.__tyhja, text="{} {}".format(k, i) ) )
                self.__kuvat[ counter ].bind( "<Button-1>", self.press )
                self.__kuvat[ counter ].grid( row=i, column=k )
                counter += 1

        self.__root.mainloop()

   #
    def press(self, event):

        #print("Klikattiin: ",event.widget)
        kuva = event.widget
        # Tämä alempi tulee olemaan avaimeni tämän ongelman ratkaisuun.
        teksti = kuva.cget('text')
        #print( teksti )

        if self.__model.tarkista_paikka( int(teksti[0]), int( teksti[2]) ):

            #print( self.__model )

            self.__tilanneLabel.config( text="Vuorossa on {}".format( self.__model.kenenVuoro() ) )

            if self.__ruksin_Vuoro:
                kuva.configure( image = self.__raksi )
                self.__ruksin_Vuoro = False
            else:
                kuva.configure( image = self.__rengas )
                self.__ruksin_Vuoro = True

        if self.__model.loppuiko():

            pelaaja = ""
            if self.__model.vuoro():
                pelaaja = "O"
            else:
                pelaaja = "X"

            loppu.LoppuRuutu( Pelaaja=pelaaja, Tasapeli=self.__model.oliko_tasapeli() )

            #self.__root.destroy()
    #
    def lopetaBtn(self):

        loppu.LoppuRuutu( Lopetti=True, Emo=self.__root )

        #self.__root.destroy()
    #
#
#Ristinollaruutu()
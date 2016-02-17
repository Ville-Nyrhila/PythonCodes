__author__ = 'Ville'

# Tein kohdat a-f.

import tkinter as tk

class Virheikkuna:
    def __init__(self, Teksti=""):
        self.__root = tk.Tk()

        self.__teksti = tk.Label( self.__root, text=Teksti )
        self.__teksti.pack()

        self.__nappi = tk.Button( self.__root, text="Ok", command=self.painaOK )
        self.__nappi.pack()

        self.__root.mainloop()

    def painaOK(self):
        self.__root.destroy()

class Käyttöliittymä:
    def __init__(self):
        self.__root = tk.Tk()

        # Koodi tähän.
        self.__pituusLabel = tk.Label( self.__root, text="Pituus(cm):" )
        self.__pituusLabel.grid( row=0, column=0 )

        self.__pituusEntry = tk.Entry( self.__root )
        self.__pituusEntry.grid( row=0, column=1 )

        self.__painoLabel = tk.Label( self.__root, text="Paino(kg):" )
        self.__painoLabel.grid( row=1, column=0 )

        self.__painoEntry = tk.Entry( self.__root )
        self.__painoEntry.grid( row=1, column=1 )

        self.__namiska = tk.Button( self.__root, text="Suorita lasku", command=self.namiskaPainettu )
        self.__namiska.grid( row=2, column=0 )

        self.__tulosLabel = tk.Label( self.__root, text="Painoindeksi tulee tähän." )
        self.__tulosLabel.grid( row=2, column=1 )

        self.__selitysLabel = tk.Label( self.__root, text="Tänne tulee selitys tuloksestasi." )
        self.__selitysLabel.grid( row=3, column=0, columnspan=2 )


        # Koodi ennen tätä. Muista.
        self.__root.mainloop()# Muista.
        # Muista.

    #
    def namiskaPainettu(self):

        pituus = self.__pituusEntry.get()

        paino = self.__painoEntry.get()

        try:
            pituus = float( pituus )
            pituus /= 100
            paino = float( paino )

            painoIndeksi = ( paino / ( pituus**2 ) )

            if paino <= 0 or pituus <= 0:
                self.nollaa()
                virhe = Virheikkuna("Paino ja pituus eivät voi olla negatiivisia tai nollia.")
            else:
                # HUOM. Wikipedian mukaan normaalin painon alaraja on 18.5. -- t. Author.
                self.__tulosLabel.config( text="{:.1f}".format( painoIndeksi ) )
                if 20 <= painoIndeksi <= 25:
                    self.__selitysLabel.config( text="Normaali paino" )
                elif painoIndeksi < 20:
                    self.__selitysLabel.config( text="Alipaino" )
                elif painoIndeksi > 25:
                    self.__selitysLabel.config( text="Ylipaino." )

        except ValueError:
            self.nollaa()
            virhe = Virheikkuna("Syötettyjen painon ja pituuden pitää olla lukuja.")

    #
    def nollaa(self):
        self.__tulosLabel.config( text="Painoindeksi tulee tähän." )
        self.__selitysLabel.config( text="Tänne tulee selitys tuloksestasi." )
    #
    def lopeta(self):
        self.__root.destroy()

def main():
    Pk = Käyttöliittymä()
#
main()
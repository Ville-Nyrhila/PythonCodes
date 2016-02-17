__author__ = 'Ville'

def main():
    suomi_espanja = {"moi": "hola", "kiitos": "gracias", "ranta": "playa"}
    lista = []
    while True:
        komento = input("[K]äännä/[L]isää/[P]oista/[T]ulosta/[Q]uit: ")

        if komento == "K":
            sana = input("Syötä käännettävä sana: ")
            if sana in suomi_espanja:
                print(sana, "espanjaksi on", suomi_espanja[sana])
            else:
                print("Sanaa", sana, "ei löydy sanakirjasta.")

        elif komento == "L":
            avain = input("Syötä lisättävä sana suomeksi: ")
            arvo = input("Syötä lisättävä sana espanjaksi: ")
            suomi_espanja[avain] = arvo

        elif komento == "P":
            poisto = input("Syötä poistettava sana suomeksi: ")
            suomi_espanja.pop(poisto)

        elif komento == "T":
            for avain in suomi_espanja:
                viiva = avain + " " + suomi_espanja[avain]
                lista.append(viiva)
            lista = sorted(lista)
            for rivi in lista:
                print(rivi)

        elif komento == "Q":
            print("Adios!")
            return

        else:
            print("Virheellinen komento, syötä joko K, L, P tai Q!")


main()
__author__ = 'Ville'

def lue_viesti():
   rivit = []
   viiva = "a"
   while( viiva != "" ):
       viiva = input()
       if viiva == "":
           pass
       else:
           rivit.append(viiva)
   return rivit
#
def tee_isoksi(rivit = []):
    viiva = ""
    palaute = []
    for rivi in rivit:
        palaute.append(rivi.upper())

    return palaute
#
def main():
    print("Syötä viestin tekstirivejä. Lopeta syöttämällä tyhjä rivi.")
    viesti = lue_viesti()

    viesti = tee_isoksi(viesti)
    print("Sama huutaen:")
    for rivi in viesti:
        print(rivi)


main()
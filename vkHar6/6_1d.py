__author__ = 'Ville'

def salaa(merkki):
    SELKOMERKIT = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                        "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w",
                        "x", "y", "z"]

    SALAMERKIT = ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y",
                            "z", "a", "b", "c", "d", "e", "f", "g", "h", "i",
                            "j", "k", "l", "m"]

    # Täydennä merkin salaaminen tähän

    i = SELKOMERKIT.index(merkki)
    merkki = SALAMERKIT[i]

    return merkki

#
def handle_merkki(m = ""):
    try:
        if m.islower():
            #print("Merkki", m, "ROT13-salattuna on:", salaa(m))
            return salaa(m)
        else:
            #print("Merkki", m, "ROT13-salattuna on:", salaa(m.lower()).upper())
            return salaa(m.lower()).upper()
    except ValueError:
        #print("Merkki", m, "ROT13-salattuna on:", m)
        return m

#
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
def salaa_rivit(rivit = []):
    palaute = []

    viiva = ""
    for rivi in rivit:
        viiva = ""
        for merkki in rivi:
            viiva += handle_merkki(merkki)
        palaute.append(viiva)

    return palaute

#
def main():
    print("Syötä viestin tekstirivejä. Lopeta syöttämällä tyhjä rivi.")
    viesti = lue_viesti()

    viesti = salaa_rivit(viesti)
    print("ROT13:")
    for rivi in viesti:
        print(rivi)


main()
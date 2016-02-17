__author__ = 'Ville'

def cout_occurences(sanakirja = {}):
    lista = []
    for sana in sanakirja:
        lista.append(str(sana) + " : " + str(sanakirja[sana]) + " kpl")
    lista = sorted(lista)
    for sana in lista:
        print(sana)
#
def create_dict(yhdiste = ""):
    lista = yhdiste.split()
    sanakirja = {}
    for sana in lista:
        sana = sana.lower()
        if sana in sanakirja:
            sanakirja[sana] += 1
        else:
            sanakirja[sana] = 1
    return sanakirja
#
def combine_lines(lines = []):
    palaute = ""
    for rivi in lines:
        palaute += rivi
        palaute += " "
    palaute = palaute[:-1]
    return palaute
#
def get_lines():
    ote = "a"
    lista = []
    print("Syötä viestin tekstirivejä. Lopeta syöttämällä tyhjä rivi.")
    while ote != "":
        ote = input()
        if ote != "":
            lista.append(ote)
    return lista
#
def main():
    rivit = get_lines()
    yhdiste = combine_lines(rivit)
    sanakirja = create_dict(yhdiste)
    cout_occurences(sanakirja)

main()
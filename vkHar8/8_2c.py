__author__ = 'Ville'

def write_file(nimi = ""):

    tiedosto = open(nimi, "w", encoding="utf-8")
    rivi = "a"
    print("Syötä viestin tekstirivejä. Lopeta syöttämällä tyhjä rivi.")

    while True:
        rivi = input()
        if rivi == "":
            break
        rivi += "\n"
        tiedosto.write(rivi)

    tiedosto.close()
    print("Tiedosto {} kirjoitettu.".format(nimi))
#
def main():
    try:
        nimi = input("Syötä tiedoston nimi: ")
        write_file(nimi)
    except Exception:
        print("Tiedoston {} kirjoittaminen epäonnistui.".format(nimi))
#
main()
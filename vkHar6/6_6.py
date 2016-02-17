__author__ = 'Ville'

def tarkista_seuraava(virke = "", a = "", i = 0):
    try:
        if virke[i+1] > a:
            a = virke[i + 1]
            i += 1
            return a + tarkista_seuraava(virke, a, i)
        else:
            return ""
    except IndexError:
        return ""
#
def funktio(fraasi = ""):

    virke = fraasi.lower()

    lause = ""

    pisin = -1
    longest_lause = ""
    a = ""

    for i in range(len(virke)):
        a = virke[i]
        lause = tarkista_seuraava(virke, a, i)
        lause = a + lause

        if len(lause) > pisin:
            pisin = len(lause)
            longest_lause = lause

    return longest_lause

#
def main():
    virke = input("Syötä merkkijono: ")
    print("Pisin aakkostettu alimerkkijono on {}".format(funktio(virke)))


main()
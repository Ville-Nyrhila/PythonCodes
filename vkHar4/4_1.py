__author__ = 'Ville'

def kysy_sademaarat():
    rivi = input("Anna sademäärä: ")
    rivi = float(rivi)
    return rivi

def main():
    ka = 0.0
    counter = 0
    print("Anna sademääriä, lopeta luvulla 999999.")
    while(True):
        luku = kysy_sademaarat()
        if (luku == 999999):
            break
        elif( luku < 0):
            pass
        else:
            ka = ka + luku
            counter += 1
    if(ka == 0):
        print("Yhtään sademäärää ei syötetty.")
    else:
        ka = ka / counter
        print("Sademäärien keskiarvo on %.1f" % ka)


main()
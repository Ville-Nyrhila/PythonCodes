__author__ = 'Ville'

def main():
    vastaus = ""
    vastaus = input("Vastaa K tai E: ")
    while(vastaus.lower() != "k"):
        if (vastaus.lower() == "e"):
            print("Vastasit",vastaus)
            break
        else:
            print("Virheellinen syöte.")
            vastaus = input("Yritä uudelleen: ")
    if (vastaus.lower() == "k"):
        print("Vastasit",vastaus)


#
main()

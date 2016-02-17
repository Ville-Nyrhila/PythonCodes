__author__ = 'Ville'

def main():
    vastaus = ""
    vastaus = input("Onko tylsää? (k/e) ")
    while(vastaus.lower() != "k"):
        if (vastaus.lower() == "e"):
            vastaus = input("Onko tylsää? (k/e) ")
        else:
            print("Virheellinen syöte.")
            vastaus = input("Yritä uudelleen: ")
    if (vastaus.lower() == "k"):
        pass
    print("Noh, lopetetaan sitten.")

main()
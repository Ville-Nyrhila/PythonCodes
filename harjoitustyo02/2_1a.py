__author__ = 'Ville'

def main():
    vastaus = ""
    while(vastaus != "k"):
        vastaus = input("Onko tylsää? (k/e) ")
        if (vastaus.lower() == "k"):
            break
    print("Noh, lopetetaan sitten.")

main()
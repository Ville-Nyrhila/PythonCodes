__author__ = 'Ville'

def main():
    kulkupelejä = ["Mersu", "Bemari", "Lada", "auto", "Audi", "kaara"]
    lista = sorted(kulkupelejä, key=str.lower)
    print(lista)

main()
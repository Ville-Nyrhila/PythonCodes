__author__ = 'Ville'

def take_list():
    print("Syötä 5 kpl lukuja:")
    lista = []
    #rivi = ""
    for i in range(5):
        rivi = input("")
        rivi = int(rivi)
        lista.append(rivi)
    return lista

def print_right_number(lista):
    luku = input("Syötä etsittävä luku: ")
    luku = int(luku)

    if luku in lista:
        print(luku,"esiintyy syöttämiesi lukujen joukossa {} kertaa.".format(lista.count(luku)))
    else:
        print("{} ei esiinny syöttämiesi lukujen joukossa.".format(luku))


def main():
    lista = take_list()
    print_right_number(lista)

main()
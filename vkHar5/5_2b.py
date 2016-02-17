__author__ = 'Ville'

def take_list():
    print("Anna 5 lukua:")
    lista = []
    #rivi = ""
    for i in range(5):
        rivi = input("Seuraava luku: ")
        rivi = int(rivi)
        lista.append(rivi)
    return lista

def print_right_number(lista):
    print("Syöttämäsi luvut päinvastaisessa järjestyksessä:")
    i = len(lista) - 1
    while i >= 0:
        print(lista[i])
        i -= 1


def main():
    lista = take_list()
    print_right_number(lista)

main()
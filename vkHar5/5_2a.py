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
    print("Syöttämäsi nollaa suuremmat luvut olivat:")
    for i in range(len(lista)):
        if (lista[i] > 0):
            print(lista[i])

def main():
    lista = take_list()
    print_right_number(lista)

main()
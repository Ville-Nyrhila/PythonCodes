__author__ = 'Ville'

def compare_list_with_self(lista = []):
    pituus = len(lista)
    for i in range(1, pituus):
        if lista[i] != lista[0]:
            return False
    return True

def take_list():
    print("Syötä 5 kpl lukuja:")
    lista = []
    #rivi = ""
    for i in range(5):
        rivi = input("")
        rivi = int(rivi)
        lista.append(rivi)
    return lista

def cout_right_number(lista):

    if compare_list_with_self(lista):
        print("Kaikki listan luvut ovat samoja.")
    else:
        print("Kaikki listan luvut eivät ole samoja.")


def main():
    lista = take_list()
    cout_right_number(lista)

main()
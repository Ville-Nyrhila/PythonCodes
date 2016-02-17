__author__ = 'Ville'

def compare_two_lists(lista, sortti):
    if len(lista) != len(sortti):
        return False
    for i in range(len(lista)):
        if lista[i] != sortti[i]:
            return False
    return True
#
def take_list():
    print("Syötä 5 kpl lukuja:")
    lista = []
    #rivi = ""
    for i in range(5):
        rivi = input("")
        rivi = int(rivi)
        lista.append(rivi)
    return lista
#
def cout_Right_number(lista):

    järjestetty = sorted(lista)

    #if compare_two_lists(lista,järjestetty):
    if lista == järjestetty:
        print("Listan alkiot ovat suuruusjärjestyksessä.")
    else:
        print("Listan alkiot eivät ole suuruusjärjestyksessä.")
#
def main():
    lista = take_list()
    cout_Right_number(lista)
#
main()
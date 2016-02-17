__author__ = 'Ville'

def cout_result(lista):
    iso = max(lista)
    pieni = min(lista)
    lista.remove(iso)
    lista.remove(pieni)
    print("Virallinen kilpailutulos on {:.2f} sekuntia.".format( sum(lista)/len(lista) ))

def take_lista():
    lista = []
    for i in range(5):
        rivi = input("Syötä {}. suorituksen aika: ".format(i + 1))
        rivi = float(rivi)
        lista.append(rivi)
    return lista

def main():
    lista = take_lista()
    cout_result(lista)

main()
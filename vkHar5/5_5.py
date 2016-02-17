__author__ = 'Ville'

def kysy_klo_aika():
    rivi = input("Mitä kello on nyt? (kokonaislukuna): ")
    rivi = int(rivi)
    return rivi
#
def tee_lista_ajoista():
    lista = [630, 1015, 1415, 1620, 1720, 2000]

    '''for i in range(24):
        tunnit = i * 100
        for k in range(4):
            minuutit = k * 15
            lista.append(tunnit + minuutit)
    '''
    return lista
#
def seur_Ajat(lista = [0], aika = 0):
    print("Seuraavat bussivuorot lähtevät:")
    raja = 3
    for i in range(len(lista)):
        if aika <= lista[i] and raja != 0:
            print(lista[i])
            raja -= 1
    if raja != 0:
        for i in range(raja):
            print(lista[i])
#
def main():
    ajat = tee_lista_ajoista()
    aika = kysy_klo_aika()
    seur_Ajat(ajat, aika)

main()
__author__ = 'Ville'

def main():
    suomi_espanja = {"moi": "hola", "kiitos": "gracias", "mennään": "vamos",
                     "ravintola": "restaurante", "missä": "donde", "ei": "no",
                     "ranta": "playa", "rannalle": "a la playa", "kyllä": "si"}

    print("Suomi-espanja:")
    for sana in sorted(suomi_espanja):
        print(sana, suomi_espanja[sana])
    print()

    #viiva = suomi_espanja

    print("Espanja-suomi:")
    for sana in sorted( suomi_espanja, key=(lambda sana : suomi_espanja[sana]) ):
        print(suomi_espanja[sana], sana)

main()

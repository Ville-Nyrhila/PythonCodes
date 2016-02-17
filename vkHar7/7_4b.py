__author__ = 'Ville'

def main():
    lista = [10, 1, 101, 2, 111, 212, 100000, 22, 222, 112, 10101, 1100, 11, 0]
    lista = sorted(lista, key=str)
    print(lista)

main()
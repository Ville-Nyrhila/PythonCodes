__author__ = 'Ville'

def salaa(merkki):
    SELKOMERKIT = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                        "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w",
                        "x", "y", "z"]

    SALAMERKIT = ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y",
                            "z", "a", "b", "c", "d", "e", "f", "g", "h", "i",
                            "j", "k", "l", "m"]

    # Täydennä merkin salaaminen tähän

    i = SELKOMERKIT.index(merkki)
    merkki = SALAMERKIT[i]

    return merkki


def main():
    m = input("Syötä merkki: ")
    try:
        if m.islower():
            print("Merkki", m, "ROT13-salattuna on:", salaa(m))
        else:
            print("Merkki", m, "ROT13-salattuna on:", salaa(m.lower()).upper())
    except ValueError:
        print("Merkki", m, "ROT13-salattuna on:", m)
main()
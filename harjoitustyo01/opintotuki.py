#__author__ = 'Ville'
tuki = input("Syötä opintotuen määrä: ")
tuki = float(tuki)
tuki *= 1.0117
print("Indeksikorotuksen ollessa 1.17 prosenttia")
print("olisi opintotuki \
 korotuksen jälkeen {} euroa".format(tuki))
print("ja jos sattuisi tulemaan vielä toinen indeksikorotus")
tuki *= 1.0117
print("olisi opintotuki sen jälkeen jo {} euroa".format(tuki))

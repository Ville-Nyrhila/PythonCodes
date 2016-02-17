__author__ = 'Ville'

luku = input("Mikä fiilis? (1-10) ")
luku = int(luku)
hymi = ""
#
if ( luku > 7 ):
    hymi = ":-)"
else:
    hymi = ":-|"

print("Tunnelmaan sopiva hymiö voisi olla", hymi,"esimerkiksi")

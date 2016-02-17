__author__ = 'Ville'

luku = input("Mikä fiilis? (1-10) ")
luku = int(luku)
hymi = ""
#
if ( luku > 10  or luku < 1):
    print("Virheellinen syöte!")
elif (luku == 10):
    hymi = ":-D"
    print("Tunnelmaan sopiva hymiö voisi olla", hymi,"esimerkiksi")
elif ( luku > 7 ):
    hymi = ":-)"
    print("Tunnelmaan sopiva hymiö voisi olla", hymi,"esimerkiksi")
elif(luku > 3):
    hymi = ":-|"
    print("Tunnelmaan sopiva hymiö voisi olla", hymi,"esimerkiksi")
elif(luku == 1):
    hymi = ":'("
    print("Tunnelmaan sopiva hymiö voisi olla", hymi,"esimerkiksi")
else:
    hymi = ":-("
    print("Tunnelmaan sopiva hymiö voisi olla", hymi,"esimerkiksi")




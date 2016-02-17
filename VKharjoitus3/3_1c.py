__author__ = 'Ville'

def agaa(luku):
    for i in range(luku):
        print("ahaa")

def säkeistö(eka, toka):
    print(eka)
    agaa(2)
    print(eka)
    agaa(2)
    print(eka)
    print(toka)
    agaa(3)

def main():
    säkeistö("saku sammakko kosiomatkallaan",
             "hän lauleli kauniita laulujaan")
    print()
    säkeistö("hän hillevi hiiren tavatessaan",
             "pyysi mukanaan tulemaan pappilaan")
    print()
    säkeistö("mikset kultasein kosinut aikanaan",
             "minut matias myyrälle naitetaan")
    print()
    säkeistö("sulle matias sovi ei laisinkaan",
             "sillä multaa on myyrällä varpaissaan")


main()
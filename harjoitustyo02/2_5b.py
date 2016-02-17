__author__ = 'Ville'

def main():
    ped = 3
    pem = 1
    switch = 0
    while(True):
        print("{}.".format(ped) + "{}.".format(pem))
        ped += 7

        if (pem < 8):
            switch = pem
        else:
            switch = pem + 1

        if (pem == 2):
            if (ped > 28):
                ped = ped - 28
                pem += 1
        elif (switch % 2 == 0):
            if (ped > 30):
                ped = ped - 30
                pem += 1
        else:
            if(ped > 31):
                ped = ped - 31
                pem += 1
        if (pem == 13):
            break

#
main()
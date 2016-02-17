__author__ = 'Ville'

def main():
    d = 1
    m = 1
    switch = 0
    for m in range(1,13):
        if (m < 8):
            switch = m
        else:
            switch = m + 1
        if (m == 2):
            for d in range(1,29):
                print("{}.".format(d) + "{}.".format(m))
        elif (switch % 2 == 0):
            for d in range(1,31):
                print("{}.".format(d) + "{}.".format(m))
        else:
            for d in range(1,32):
                print("{}.".format(d) + "{}.".format(m))
#
main()
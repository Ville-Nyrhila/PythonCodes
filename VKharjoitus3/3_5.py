__author__ = 'Ville'

def take_input(kys):
    luku = -1
    while luku <= 0:
        luku = input(kys)
        luku = int(luku)
    return luku

def take_input_allow_zero(kys):
    luku = -1
    while luku < 0:
        luku = input(kys)
        luku = int(luku)
    return luku

def main():
    paino = take_input("Potilaan paino (kg): ")
    aikaa = take_input("Kauanko aikaa edellisestä annoksesta (tasatunteina): ")

    voiottaa = paino * 15

    kokannos = take_input_allow_zero("Kokonaisannos viimeisen 24 tunnin aikana (mg): ")
    voiantaa = 0
    if(kokannos >= 4000):
        pass
    elif (aikaa >= 6):
        voiantaa = 4000 - kokannos
        if(voiantaa < voiottaa):
            pass
        else:
            voiantaa = voiottaa
    print("Potilaalle voi antaa parasetamolia: %i" % voiantaa)

main()
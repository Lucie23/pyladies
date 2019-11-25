from random import randrange

import util

def tah_pc(pole):
    symbol = 'O'
    cislo_pole = randrange(20)
    if pole[cislo_pole] == '-':
        print('Pocitac zvolil toto pole')
        pole = tah(pole, cislo_pole, symbol)    
        return pole
    return tah_pc(pole)
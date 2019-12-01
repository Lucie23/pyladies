from util import tah
from ai import tah_pc

pole = '--------------------'
cislo_pole = False
symbol = 'X' or 'O'

def tah_clovek(pole, cislo_pole):
    symbol = 'X'
    pole_list = list(pole)
    while True:
        try:
            cislo_pole = int(input('Vyber si pole a zadej cislo:'))
            break
        except ValueError:
            print('Musis zadat cislo.')
            continue
    if cislo_pole in range(0, 20):
        if pole_list[cislo_pole] == '-':
            print('Tvuj tah.')
            pole = tah(pole, cislo_pole, symbol)            
            return pole
        else:
            print('Toto pole je obsazene, vyber jine.')
            return tah_clovek(pole, cislo_pole)
    else:
        print('Toto pole neexistuje, vyber jine.')
    return tah_clovek(pole, cislo_pole)

def vysledek_hry(pole):
    if 'OOO' in pole:
        print('pocitac vyhral')
        return False
    elif 'XXX' in pole:
        print('vyhrala jsi')
        return False
    elif '-' not in pole:
        print('remiza')
        return False
    else:
        print('hra jeste neskoncila')
        return True

def hra(pole):
    print('Nyni si zahrajeme piskvorky. Hrac ma symbol X a pocitac O.')
    while '-' in pole:
        if vysledek_hry(pole) == False:
            break
        else:
            pole = tah_clovek(pole, cislo_pole)
        if vysledek_hry(pole) == False:
            break
        else:
            pole = tah_pc(pole)
    if '-' not in pole:
        vysledek_hry(pole)
    return print('Hra skoncila.')

hra(pole)
import ai, util, piskvorky
import pytest
from random import randrange


def test_tah():
    pole = util.tah(0, 'X', '--------------------')
    assert len(pole) == 20

def test_tah_clovek():
    pole = piskvorky.tah_clovek(0, '--------------------')
    assert pole.count('X') == 1
    assert pole.count('-') == 19


def test_vysledek_hry():
    assert piskvorky.vysledek_hry('-----XXX------------') == ('Vyhrala jsi')
    assert piskvorky.vysledek_hry('-------------OOO----') == ('Pocitac vyhral')
    assert piskvorky.vysledek_hry('XXOOXXOOXXOOXXOOXXOO') == ('Remiza')

    
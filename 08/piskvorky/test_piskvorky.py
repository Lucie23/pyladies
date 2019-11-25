import ai, util, piskvorky

def test_tah():
    pole = util.tah(0, 'X', '--------------------')
    assert len(pole) == 20

def test_tah_pc():
    pole = ai.tah_pc('O', '--------------------')
    assert pole.count('O') == 1
    assert pole.count('-') == 19

def test_vysledek_hry():
    assert piskvorky.vysledek_hry('-----XXX------------') == ('Vyhrala jsi')
    assert piskvorky.vysledek_hry('-------------OOO----') == ('Pocitac vyhral')
    assert piskvorky.vysledek_hry('XXOOXXOOXXOOXXOOXXOO') == ('Remiza')

    
def tah(pole, cislo_pole, symbol):
    pole_list = list(pole)
    pole_list[cislo_pole] = symbol
    pole = "".join(pole_list)
    print(pole)
    return pole
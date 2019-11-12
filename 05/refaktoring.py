cislo = input('Zadej rodne cislo ve spravnem formatu:')
pocet_cisel = (cislo.replace('/',''))

def length(cislo):
    if len(cislo) == 11:
        return True
    else:
        return False
print(length(cislo))

def slash(cislo):
    if cislo[6] != '/':
        return True
    else:
        return False
print(slash(cislo))

def division(cislo):
    if int(pocet_cisel) % 11 == 0:
        return True
    else:
        return False
print(division(cislo))

def format(cislo):
    if pocet_cisel.isnumeric():
        return True
    else:
        return False
print(format(cislo))
rodne_cislo = input('Zadej rodne cislo:')
# spravny format: 6 cislic, /, 4 cislice
format_cisla = rodne_cislo[:6] + rodne_cislo[7:]

den = rodne_cislo[4:6]
mesic = '12'
rok = '19' + str(rodne_cislo[:2])
narozeni = int(rodne_cislo[2:4])

def format(rodne_cislo):
    return len(rodne_cislo) == 11 or rodne_cislo[6] == '/' or rodne_cislo[:6].isdigit() or rodne_cislo[7:].isdigit()
print (format(rodne_cislo))

def delitelne_11(rodne_cislo):
    format_cisla = rodne_cislo[:6] + rodne_cislo[7:]
    return int(format_cisla) % 11 == 0
print (delitelne_11(rodne_cislo))

def datum_narozeni(rodne_cislo):
    if narozeni > 12:
        mesic = narozeni - 50
    else:
        mesic = narozeni   
    return (den, mesic, rok)
print (datum_narozeni(rodne_cislo))

def pohlavi(rodne_cislo):
    if narozeni > 12:
        return ('Zena')
    else:
        return ('Muz')
print (pohlavi(rodne_cislo)) 
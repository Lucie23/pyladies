rodne_cislo = input('Zadej rodne cislo ve spravnem formatu:')
# spravny format: 6 cislic, /, 4 cislice

format_cisla = rodne_cislo[:6] + rodne_cislo[7:]

try:
    if len(rodne_cislo) != 11:
        raise IndexError
except IndexError:
    print('Cislo neobsahuje pozadovany pocet znaku.')
   
try:
    if rodne_cislo[6] != '/':
        raise TypeError
except TypeError:
    print("Cislo neobsahuje '/' na spravnem miste.")
   
try:
    if int(format_cisla) % 11 != 0:
        raise ValueError
except ValueError:
    print('Cislo neni delitelne jedenacti.')
   
try:    
    if not rodne_cislo[:6].isdigit():
        raise TypeError
except TypeError:
    print('Cislo neobsahuje spravne znaky.')
  
try:
    if not rodne_cislo[7:].isdigit():
        raise TypeError
except TypeError:
    print('Cislo nema pozadovane znaky.')
    
else:
    print('Toto cislo je napsano spravne.')
    
rodne_cislo = input('Zadej rodne cislo ve spravnem formatu:')
# spravny format: 6 cislic, /, 4 cislice

format_cisla = rodne_cislo[:6] + rodne_cislo[7:]

if len(rodne_cislo) != 11:
    print('Cislo neobsahuje pozadovany pocet znaku.')

elif rodne_cislo[6] != '/':
    print("Cislo neobsahuje '/' na spravnem miste.")

elif int(format_cisla) % 11 != 0:
    print('Cislo neni delitelne jedenacti.')

elif not rodne_cislo[:6].isdigit():
    print('Cislo neobsahuje spravne znaky.')

elif not rodne_cislo[7:].isdigit():
    print('Cislo nema pozadovane znaky.')

else:
    print('Toto cislo je napsano spravne.')
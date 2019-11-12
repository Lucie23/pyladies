while 1==1:
    cislo = input('Zadej rodne cislo ve spravnem formatu:')
    # spravny format: 6 cislic, /, 4 cislice
    pocet_cisel = (cislo.replace('/',''))
    cislo_1 = pocet_cisel[:6]
    cislo_2 = pocet_cisel[6:]
    if len(cislo) != 11:
        print('Cislo neobsahuje pozadovany pocet znaku.')
        continue
    elif cislo[6] != '/':
        print('Cislo neobsahuje '/' na spravnem miste.')
        continue
    elif int(pocet_cisel) % 11 != 0:
        print('Cislo neni delitelne jedenacti.')
        continue
    elif not cislo_1.isnumeric():
        print('Cislo nema pozadovane znaky.')
        continue
    elif not cislo_2.isnumeric():
        print('Cislo nema pozadovane znaky.') 
        continue
    else:
        break 

print('Toto je platne rodne cislo.') 
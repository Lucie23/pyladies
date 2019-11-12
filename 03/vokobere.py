from random import randrange

pocet = 0
while pocet < 21:
    print('Máš', pocet, 'bodů')
    odpoved = input('Chceš otočit další kartu?')
    if odpoved == 'ano':
        karta = randrange(2, 11)
        print('Otočila jsi', karta)
        pocet = pocet + karta
    elif odpoved == 'ne':
        print('Prohrála jsi')
        break
    else:
        print('Nerozumím!')

if pocet == 21:
    print('Vyhrála jsi!')
elif pocet > 21:
    print('Smůla!', pocet, 'bodů je moc!')
else:
    print('Chybělo ti', 21 - pocet, 'bodů!')
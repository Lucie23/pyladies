zvirata = ['pes', 'kocka', 'kralik', 'had', 'andulka']
druhe_pismeno = []
dvojice = []
serazeny_seznam = []

for zvire in zvirata:
    druhe_pismeno.append(zvire[1])
    dvojice.append((zvire[1], zvire))
    continue

druhe_pismeno.sort()
dictionary = dict(dvojice)

for x in druhe_pismeno:
    if x in dictionary:
        serazeny_seznam.append(dictionary[x])
        continue

print(serazeny_seznam)
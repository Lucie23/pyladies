#Cesarova šifra
vstup = input('Zadej text:')
posun = 4
sifra = ''
for znak in vstup:
    novyznak = znak
    if 'a' <= znak <= 'z':
        novyznak = chr((ord(znak)-
97+posun)%26 + 97 )
    sifra = sifra+novyznak
print(sifra)
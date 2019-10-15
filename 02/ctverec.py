strana = float(input ('Zadej stranu čtverce v centimetrech:'))
cislo_je_spravne = strana > 0
if cislo_je_spravne:
    print('obvod ctverce se stranou', strana, 'je', 4*strana, 'cm')
    print('obsah ctverce se stranou', strana, 'je', strana**2, 'cm2')
else:
    print ('strana musi byt kladna')

barvy_ovoce = {
    'hruška': 'zelená',
    'jablko': 'červená',
    'meloun': 'zelená',
    'švestka': 'modrá',
    'ředkvička': 'červená',
    'zelí': 'zelená',
    'mrkev': 'červená',
}

barvy_ovoce_po_tydnu = dict(barvy_ovoce)

for klic in barvy_ovoce_po_tydnu:
    barvy_ovoce_po_tydnu[klic] = 'černo-hnědo-' + barvy_ovoce_po_tydnu[klic]

print (barvy_ovoce['jablko'])
print (barvy_ovoce_po_tydnu['jablko'])                                          
                                
from random import randrange

tah_pc = randrange (3)

#0 kámen, 1 nůžky, 2 papír

tah_clovek = input ('kámen, nůžky, nebo papír?')

if tah_pc == 0:
    print ('Počítač si vybral kámen.')

elif tah_pc == 1:
    print ('Počítač si vybral nůžky.')

elif tah_pc == 2:
    print ('Počítač si vybral papír.')


if (tah_pc == 0 and tah_clovek == 'kámen') or (tah_pc == 1 and tah_clovek == 'nůžky') or (tah_pc == 2 and tah_clovek == 'papír'):
    print ('Plichta.')

elif (tah_clovek == 'kámen' and tah_pc == 2) or (tah_clovek == 'nůžky' and tah_pc == 0) or (tah_clovek == 'papír' and tah_pc == 1):
    print ('Počítač vyhrál.')

elif (tah_clovek == 'kámen' and tah_pc == 1) or (tah_clovek == 'nůžky' and tah_pc == 2) or (tah_clovek == 'papír' and tah_pc == 0):
    print ('Vyhrála jsi!')

else:
    print ('Nerozumím.')
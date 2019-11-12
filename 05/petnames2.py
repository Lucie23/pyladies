animals = {'Nemo' : 'fish', 'Jerry' : 'mouse', 'Tom' : 'cat'}

for name, animal in animals.items():
    print('{} is a {}.'.format(name, animal))

def animal_printing(a):
    print('Print from the function:')
    for name, animal in animals.items():
        print('{} is a {}.'.format(name, animal))

animal_printing(animals)
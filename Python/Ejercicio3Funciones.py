def añoBisiesto():
    anno = int(input("Introduce el año que deseas ver "))

    if anno % 4 == 0 and (anno % 100 != 0 or anno % 400 == 0):
        print('El año ', anno,' es bisiesto')
    else:
        print('El año ', anno,' no es bisiesto')

print('Determinando si un año es bisiesto')
añoBisiesto()
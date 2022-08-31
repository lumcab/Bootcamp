from functools import reduce
from traceback import print_tb


def suma(a, b):
    print(f'a={a}, b={b}')
    return a + b


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

impares = list(filter((lambda x: x % 2 !=0 ), numeros))

print('numeros impares de la lista', list(impares))


resultado = reduce(suma, impares)

print(resultado)

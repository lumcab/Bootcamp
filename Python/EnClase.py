# esta seccion es para la clase

from functools import reduce


def main():
    print('in class')

    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def mifuncion(x):
        if x % 2 == 0:
            return True
        return False

    # Filter se ejecuta sobre los elementos que cumplan la funcion de una lista
    resultado = filter(mifuncion, numeros)

    # Usando una funcion anonima
    resultado2 = filter(lambda x: x % 2 == 0, numeros)

    print(list(resultado))
    print(list(resultado2))

    # map se ejecuta la funcion indiscrimandamente sobre cada elemento de una lista
    resultado3 = map(lambda x: x * x, numeros)

    print(list(resultado3))

    # reduce se usa para contar una lista o reducir al minimo uns lista
    def suma(a, b):
        print(f'a={a}, b={b}')
        return a + b

    resultado4 = reduce(suma, numeros)

    print(resultado4)

    # Redondear valores round
    a=3.6
    print(round(a))

    # Para hallar el valor minimo usamos min
    print(min(numeros))

    


if __name__ == '__main__':
    main()

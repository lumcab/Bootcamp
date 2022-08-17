def numeroPrimo():
    number = int(input('Introduce el numero: '))
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                print('el numero ', number, ' NO ES PRIMO. Es divisible entre ', i)
                break
        else:
            print('el numero ', number, ' ES PRIMO')
    else:
        print('el numero debe ser mayor que 1')

print('Para determinar si un numero es primo')
numeroPrimo()
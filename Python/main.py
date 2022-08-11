import Calculadora as c

def init():

    suma = c.sumar(2,5)
    print(f"El resultado de la suma es {suma}")

    resta = c.restar(5,2)
    print(f"El resultado de la resta es {resta}")

    multiplica = c.multiplicar(2,5)
    print(f"El resultado de la multiplicacion es {multiplica}")

    divide = c.dividir(6,2)
    print(f"El resultado de la divicion es {divide}")
    
if __name__ == '__main__':
    init()

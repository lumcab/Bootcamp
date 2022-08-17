import math

def areaTriangulo(base, altura):
    return (base*altura)/2

def areaCirculo(radio):
    return (radio**2)*math.pi

print('Para calcular el area de un triangulo debe indicar los valores de su base y altura')
base = float(input("indique el valor de la base el triangulo: "))
altura = float(input('indique el valor de la altura: '))
print('El area del triangulo es ', areaTriangulo(base,altura))

print('Para calcular el area de un circulo debe indicar el valor de su radio')
radio = float(input("indique el valor del radio del circulo: "))
print('El area del circulo es ', areaCirculo(radio))

#Funciones con parametros variables
def suma(*args): #Crea una tupla con los datos
    print(args)
    resultado=0
    for arg in args:
        resultado+=arg
    print(resultado)
suma(3,5,2,8,6,5)

def suma(**kwargs): #Crea un diccionario con los datos
    print(kwargs)
    for key, value in kwargs.items():
        print(key, "=", value)
suma(vivienda='casa', coche = 'rojo')


def operaciones(a,b):
    return a+b,a-b,a*b,a/b

suma, resta, multi, divi = operaciones(8,4)
print(suma)
print(resta)
print(multi)
print(divi)
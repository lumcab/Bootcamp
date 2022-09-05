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

def sumador(** kwargs):
    inicial=kwargs['inicial'] if 'inicial' in kwargs else 1
    final=kwargs['final'] if 'final' in kwargs else 1
    resultado=0
    for x in range(inicial,final+1):
        resultado+=x
    return resultado

print(sumador())
print(sumador(inicial=15,final=30))

def operaciones(a,b):
    return a+b,a-b,a*b,a/b

resultado = operaciones(8,4) #se guarda el resultado en una tupla
print(resultado)
print(resultado[0])
print(resultado[1])
print(resultado[2])
print(resultado[3])
suma, resta, multi, divi = operaciones(8,4)
print(suma)
print(resta)
print(multi)
print(divi)

#funciones anonimas o lambda
anonima = lambda funcion: print(funcion,'es una funcion lambda')

anonima('anonima')

sumatoria= lambda x:x+x
print(sumatoria(2))
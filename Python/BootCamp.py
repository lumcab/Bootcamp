# Informacion importante que he visto en el bootcamp
#no olvidar estudiar diariamente

lista=[1,2,3,'a']
longitud=len(lista)
print("Ciclos for")
print("La lista tiene",longitud,"items")
#for en python
for numero1 in lista:
    print (numero1)
# [5 a 11) el for con range recorre asi los parametros
print("for con range")
for numero in range(5,11):
    print(numero)
#else en for
listafor = ["hola", "adios"]
for palabra in listafor:
    if palabra == "mensaje":
        print("Encuentro la palabra mensaje")
        break
else:
    print("no encuentro nada")
#ordenar una lista
lista1=[3,6,5,1,2,4]
print(lista1)
print("lista ordenada")
listaordenada = sorted(lista1)
print(listaordenada)
print("lista ordenada de revez")
listaordenadar = sorted(lista1, reverse=True)
print(listaordenadar)

#hacer swich en python
valor = 11
match valor:
    case 1:
        print("valor es igual a 1")
    case 2:
        print("valor es igual a 2")
    case 3:
        print("valor es igual a 3")
    case 4:
        print("valor es igual a 4")
    case 5:
        print("valor es igual a 5")
    case _:
        print("valor indeterminado")

#para corta algo si que tenga que cumplir usamos pass
if 5 < 6:
    pass

#agregar un enter al final de cada linea de una lista si no lo tiene
def escribe (fichero,datos):
    f = open(fichero, 'a')
    for linea in datos :
        if not linea.endswith (' \n '):
                linea += '\n'
        f.write (linea)
    f.close ()

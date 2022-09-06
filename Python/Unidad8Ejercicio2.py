#Ejercicio 2 de la unidad 8 de python

def main():

    class Vehiculo:
        def tipo(self,tipo):
            a = 'Este vehicuo es del tipo '+tipo +'\n'
            return a

    def escribir(x):
        f = open('vehiculos.txt','a')
        f.write(x)
        f.close()

    def leer():
        f = open('vehiculos.txt','r')
        datos = f.readlines()
        f.close()
        return datos

    def imprimir():
        imprimir = leer()
        for i in imprimir:
            print(i)

    vehiculo = Vehiculo()
    v1 = vehiculo.tipo('automovil')
    escribir(v1)
    v2 = vehiculo.tipo('motocicleta')
    escribir(v2)
    imprimir()

if __name__ == '__main__':
    main()
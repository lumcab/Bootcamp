#Ejercicio 1 de la unidad 8 de python
def main():

    def escribir(lista):
        f = open('archivo.txt','w')
        for i in lista:
            if not i.endswith (' \n '):
                i += '\n'
            f.write(i)
        f.close()

    def leer():
        f = open('archivo.txt','r')
        datos = f.readlines()
        f.close()
        return datos

    def imprimir():
        imprimir = leer()
        for i in imprimir:
            print(i)

    lista = ['esta es la informacion', 'que se guarda en el archivo', 'que consta de tres elementos']
    escribir(lista)
    imprimir()
    imprimir()

if __name__ == '__main__':
    main()
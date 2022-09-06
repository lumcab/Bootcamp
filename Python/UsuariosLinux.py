# programa creado para buscar usuarios en el sistema linux
def main():
    usuarios = listarusuarios()
    for usuario in usuarios:
        print(f'usuario: {usuario}')

def listarusuarios():
    salida = []
    f = open('/etc/passwd', 'r')
    datos = f.readlines()
    f.close()
    #determinar usuarios reales y no del sistema
    for linea in datos:
        partes = linea.split('/')
        if partes[-1] == 'nologin\n':
            continue
        parte = linea.split(':')

        salida.append(parte[0])
    return salida

if __name__ == '__main__':
    main()
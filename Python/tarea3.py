nombre = 'Alejandra'
apellidos = "Penagos Cabrera"
edad = 28
email = 'alejapeca@gmail.com'
telefono = 32165498765
casado = False
conHijos = False
listaDeAmigos = ['miguel', 'luis', 'felipe', 'laura', 'catalina']
películasVistas = {'pelicula1':'Thor3','pelicula2':'Doctor estrange', 'pelicula3':'Harry Potter1','pelicula4':'Harry Potter2'}
print('Nombre: ',nombre)
print('Apellidos: ',apellidos)
print('Edad: ',edad)
print('Email: ',email)
print('Telefono: ',telefono)
print('Esta casada: ',casado)
print('Tiene hijos: ',conHijos)
print('Nombre algunos amigos: ',listaDeAmigos)
print('Ultimas peliculas vistas: ',películasVistas)
peso = float(input("cuanto pesa en kilogramos?: "))
estatura = float(input("cuanto mide en centimetros?: "))/100
imc = peso/estatura**2
imc2 = round(imc, 2)
print('Su indice de masa corporal es : ',imc2)

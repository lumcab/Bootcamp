#mayor de edad
edad = int(input("cuantos años tienes: "))

if edad > 17 and edad <121:
    print("usted es mayor de edad")
elif edad > 120 or edad <= 0:
    print("usted ya esta muerto o no existe")
else:
    print("usted es menor de edad")
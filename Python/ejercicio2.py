print("Numeros impares")
print("seleccione el rango deseado")
number1 = int(input("primer numero: "))
number2 = int(input("segundo numero: "))
contador = 0
for numero in range(number1,number2+1):
    if numero % 2 == 0:
        continue
    else:
        print ('el numero' , numero,'es impar')
        contador += 1
print('entre los numeros ',number1, "y ", number2, "hay ", contador, "numeros impares")
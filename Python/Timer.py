import time

hora = time.strftime('%H')
minutos = time.strftime('%M')

if int(hora) >= 19:
    print (f"Son las {hora}:{minutos}")
    print ("Es hora de irse a casa")
else:
    print (f"Son las {hora}:{minutos}")
    print ("Quedan {} horas y {} minutos para irnos a casa".format(18- int(hora), 59-int(minutos)))

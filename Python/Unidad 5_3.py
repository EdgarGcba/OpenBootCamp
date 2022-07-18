def bisiesto(anio):
    return anio % 4 ==0 and (anio % 100 != 0 or anio % 400 ==0)

    


if bisiesto(2023):
    print('El anio Es bisiesto')
else:
    print('El anio No Es bisiesto')
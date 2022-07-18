from math import pi

def areaTriangulo(base, altura):
    return base*altura

def areaCirculo(radio):
    return round(pi*radio**2, 2)

triangulo = areaTriangulo(4, 5)
circulo = areaCirculo(10)

print('El area del triangulo es ',  str(triangulo))
print('El area del Circulo es ',  str(circulo))
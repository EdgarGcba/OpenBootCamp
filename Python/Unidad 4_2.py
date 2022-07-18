numInicio = int(input('Ingrese numero inicial...'))
numFin = int(input('Ingrese numero final...'))
while (numFin>=numInicio):
    if (numInicio%2 == 0):
        print('El numero es par ' + str(numInicio))
        numInicio +=2
        continue
    else:
        numInicio += 1

        
f = open('info .txt','w' )
datos = f.write('Nombre: \n')
datos = f.write('Apellido: \n')
f.close()

f = open('info .txt','a' )
datos = f.write('Direccion: \n')
datos = f.write('Celular: \n')
f.close()



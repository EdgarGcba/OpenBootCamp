from datetime import datetime


fecha_y_hora = datetime.now()

hora_actual  = fecha_y_hora.time()
hora = int(fecha_y_hora.strftime("%H"))
minutos = int(fecha_y_hora.strftime("%M"))

if (int(hora_actual.strftime("%H" "%M"))) > 1900:
    print('Es hora de ir a casa')
else:
    print(f"Aun faltan {19 - hora} horas y {60 - minutos} minutos para ir a casa")
    



"""En este ejercicio tenéis que crear una lista de RadioButton que muestre la opción que se ha seleccionado y que contenga un botón de reinicio para que deje todo como al principio.

Al principio no tiene que haber una opción seleccionada."""
import tkinter
from tkinter import ttk

def mi_seleccion():
    pass
window = tkinter.Tk()

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

selected = tkinter.StringVar()
radioB_1 = ttk.Radiobutton(window, text='Python', value='1', variable=selected, command=mi_seleccion)
radioB_1.grid(column=0, row=1, padx=5, pady=5)

radioB_2 = ttk.Radiobutton(window, text='JavaScript', value='2', variable=selected, command = mi_seleccion)
radioB_2.grid(column=0, row=2, padx=5, pady=5)

radioB_3 = ttk.Radiobutton(window, text='Java', value='3', variable=selected, command = mi_seleccion)
radioB_3.grid(column=0, row=3, padx=5, pady=5)


boton = tkinter.Button(window, text='Submit')
boton.grid(column=1, row =3, padx=5, pady=5)
boton.bind('<Button-1>', )


window.mainloop()
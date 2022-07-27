from cgitb import text
"""En este ejercicio tenéis que crear una lista de RadioButton que muestre la opción que se ha seleccionado y que contenga un botón de reinicio para que deje todo como al principio.

Al principio no tiene que haber una opción seleccionada."""
import tkinter
from tkinter import ttk

window = tkinter.Tk()

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

user_name = ttk.Label(window, text='Username:')
user_name.grid(column=0, row=0, sticky=tkinter.W, padx=5, pady=5)

user_name_entry = ttk.Entry(window, )
user_name_entry.grid(column=1, row=0, sticky= tkinter.E, padx=5, pady=5)

user_pass = ttk.Label(window, text='Password:')
user_pass.grid(column=0, row=1, sticky=tkinter.W, padx=5, pady=5)

user_pass_entry = ttk.Entry(window, show='*')
user_pass_entry.grid(column=1, row=1, sticky= tkinter.E, padx=5, pady=5)

login_button = ttk.Button(window, text='Submit')
login_button.grid(column=1, row=3, sticky=tkinter.E, padx=5, pady=5)



window.mainloop()


from mailbox import NoSuchMailboxError


class Alumno:
    def __init__(self, nombre, apellido, nota):
        self.nombre = nombre 
        self.apellido = apellido
        self.nota = nota
    
    def __str__(self):
        return f"Nombre {self.nombre}, Apellido {self.apellido}, Nota {self.nota}"
    
    def aprobo(self):
        if self.nota >= 6:
            return f"El Alumno aprobo"
        else:
            return f"El alumno reprobo"
        
        
        
alumno1 = Alumno('Roxana', 'Queen', 9)
print(alumno1)
print(alumno1.aprobo())

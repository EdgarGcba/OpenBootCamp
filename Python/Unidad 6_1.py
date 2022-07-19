
class Vehiculo:
    
    
    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.puertas = puertas
        self.ruedas = ruedas
    def __str__(self):
        return f"Soy un vehiculo de: color {self.color}, {self.ruedas} ruedas y {self.puertas} puertas"

class Coche(Vehiculo):
    
    
    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        super().__init__(color, ruedas, puertas)
        self.cilindrada = cilindrada
        self.velocidad = velocidad
    def __str__(self):
        return f"Soy un vehiculo de: color {self.color}, {self.ruedas} ruedas , {self.puertas} puertas, {self.cilindrada} cc, {self.velocidad} velocidad"
        
        
dodge = Coche("Blanco", 4, 2, 0, 1600)
print(dodge)

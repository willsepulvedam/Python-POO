class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    
    def imprimir(self):
        print(f"\nNombre: {self.nombre}\n")
        print(f"Edad: {self.edad}\n")
 
        
         
    def mayor_de_edad(self):
        if self.edad >= 18:
            print("mayor de edad")
        else:
            print("menor de edad")
        
        

will = Persona("will",17)


will.imprimir()
will.mayor_de_edad()
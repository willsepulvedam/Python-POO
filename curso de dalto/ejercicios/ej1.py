class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    
    
    def imprimir(self):
        print(f"""
              Nombre: {self.nombre}
              nota: {self.nota}
              """)  
        
         
    def aprobado(self):
        if self.nota >= 3.0:
            print("aprobado")
        else:
            print("reprovado")
        
        

will = Alumno("will", 3.8)


will.imprimir()
will.aprobado()

            
        
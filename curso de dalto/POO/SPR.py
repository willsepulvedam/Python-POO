#creamos la clase tanquedecombustible para encargarnos espesificamente del combustible del auto
class TanqueDeCombustible:
    #creamos el constructor con el atributo combustible
    def __init__(self):
        self.combustible = 100
    
    #funcion que nos permite agregar combustible al tanque
    def agregar_comustible(self, cantidad):
        self.combustible += cantidad
    
    #funcion para mostrar el combustible
    def obtener_combustible(self):
        return self.combustible
    
    #funcion que nos permite darle combustible a el auto
    def usar_combustible(self, cantidad):
        self.combustible -= cantidad

#creamos la clase del auto con los atributos de posicion y el tanque que ya creamos 
class Auto:
    def __init__(self, tanque):
        self.posicion = 0
        self.tanque = tanque
    
    #funcion que nos permite movernos y a su ves ir restando el combustible del auto
    def mover(self, distancia):
        if self.tanque.obtener_combustible() >= distancia / 2:
            self.posicion += distancia
            self.tanque.usar_combustible(distancia / 2)
            print("Has movido exitosamente el auto!")
        else:
            print("No hay suficiente combustible")
    
    #funcion para mostrar la posicion del auto despues de moverlo
    def obtener_posicion(self):
        return self.posicion
    

        
tanque = TanqueDeCombustible()
auto = Auto(tanque)

print(auto.obtener_posicion())
auto.mover(10)
print(auto.obtener_posicion())
auto.mover(20)
print(auto.obtener_posicion())
auto.mover(60)
print(auto.obtener_posicion())
auto.mover(100)
print(auto.obtener_posicion())
auto.mover(100)
       
            
        
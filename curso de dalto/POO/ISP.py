#importamos abc para crear las clases y funciones abstractas
from abc import ABC, abstractmethod

#creamos la clase trabajador para que trabaje
class Trabajador(ABC):
    
    @abstractmethod
    def trabajar(self):
        pass
    
#creamos la clase comedor para que coma
class Comedor(ABC):
    
    @abstractmethod
    def comer(self):
        pass
    
#creamos la clase durmiente para que duerma
class Durmiente(ABC):
    
    @abstractmethod
    def dormir(self):
        pass
    
    
#creamos una clase humano y heredamos las clases anteriores ya que un humano hace todas
#esa funciones
class Humano(Trabajador, Durmiente, Comedor):
    def comer(self):
        print("el humano esta comiendo")
        
    def trabajar(self):
        print("el humano esta trabajando")
        
    def dormir(self):
        print("el humano esta durmiendo")

#en cambip creamos la clase robot y solo heredamos la clase trabajador ya que un robot
#no come ni duerme   
class Robot(Trabajador):
   
         
    def trabajar(self):
        print("el robot esta trabajando")
      
    

robot = Robot()  

robot.trabajar()
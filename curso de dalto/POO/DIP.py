# class Diccionario:
#     def verificar_palabras(self, palabra):
#         #logica para verificar palabras
#         pass
    
# class CorrectorOrtografico:
#     def __init__(self):
#         self.diccionario = Diccionario()
        
#     def corregir_texto(self, texto):
#         #logica para corregir texto
#         pass

from abc import ABC, abstractmethod

class VerificadorOrtografico(ABC):
    @abstractmethod
    def verificar_palabra(self, palabra):
        pass
    
class Diccionario(VerificadorOrtografico):
    def verificar_palabra(self, palabra):
        #logica para verificar palabras si esta en el diccionario
        pass

class ServicioOnline(VerificadorOrtografico):
    def verificar_palabra(self, palabra):
        #logica para verificar palabras desde el servicio web
        pass
    
class CorrectorOrtografico:
    def __init__(self, verificador):
        self.verificador = verificador
        
    def correfir_texto(self, texto):
        #usamos el verificador para corregir texto
        pass
#creado el decorador
def decorador(funcion):
    def funcion_modificada():
        print("Antes de ejecutar la función")
        funcion()
    return funcion_modificada

#forma no oprima de hacer un decorador

# def saludo():
#     print('Hola mundo')
    
# saludo_modificado = decorador(saludo)
# saludo_modificado()

#forma oprima de hacer un decorador
@decorador
def saludo():
    print('hola mundo')
    
saludo()


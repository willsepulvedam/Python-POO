
#funcion para obtener el profesor y su asistente segun su edad
def obtener_compañeros(cantidad_de_compañeros):
    
    #crear la lista para los compañeros
    compañeros = []

    #ejecutando un for para pedir los datos de los compañeros
    for i in range (cantidad_de_compañeros):
        nombre = input("decime tu nombre: ")
        edad = int(input("decime tu edad pa:"))
        compañero = (nombre, edad)

        #agregando la informacion a la lista
        compañeros.append(compañero)
    
    #ordenandolos de menor a mayor segun su edad
    compañeros.sort(key=lambda x:x[1])

    #comapañeros[x] devuelve una tupla con (nombre, edad) y accedemos a el nombre para definir al asistente y profesor
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]
    
    #rertornar la tupla
    return asistente,profesor

#desempaquetar lo que nos retorna la funcion
asistente,profesor = obtener_compañeros(5)

#imprimimos el resultado
print (f"el profesor es: {profesor} y su asistente es: {asistente}.")

    
    



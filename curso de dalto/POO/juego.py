class Personaje:
    def __init__(self, nombre, fuerza, velocidad):
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad
    
    def __repr__(self):
        return f"{self.nombre} (Fuerza: {self.fuerza} Velocidad: {self.velocidad})"
    
    def __add__(self, otro_pj):
        nuevo_nombre = self.nombre + "-" + otro_pj.nombre
        nueva_fuerza = round(((self.fuerza + otro_pj.fuerza)/2)**1.34)
        nueva_velocidad = round(((self.velocidad + otro_pj.velocidad)/2)**1.34)
        return Personaje(nuevo_nombre, nueva_fuerza, nueva_velocidad)
    
def mostrar_personajes(personajes):
    if not personajes:
        print("aun no hay ningun personaje.")
    else:
        print("personajes disponibles:")
        for i, personaje in enumerate(personajes):
            print(f"{i + 1}. {personaje}")
            
def crear_personaje():
    nombre = input("Ingrese el nombre del personaje: ")
    fuerza = float(input("Ingrese la fuerza del personaje: "))
    velocidad = float(input("Ingrese la velocidad del personaje: "))
    return Personaje(nombre, fuerza, velocidad)

personajes = []

while True:
    print("\n1. Crear Personaje")
    print("2. Fusionar personajes")
    print("3. Mostrar personajes")
    print("Salir")
    opcion = input("Seleccione una opcion: ")
    
    if opcion == "1":
        personaje_nuevo = crear_personaje()
        personajes.append(personaje_nuevo)
        print("Personaje creado con exito!")
        
    
    elif opcion == "2":
        if len(personajes) < 2:
            print("debe tener almenos dos personajes para fusionar.")
        else:
            mostrar_personajes(personajes)
            num_pj1 = int(input("Ingrese el numero del primer personaje: "))
            num_pj2 = int(input("Ingrese el numero del segundo personaje: "))
            
            if 1 <= num_pj1 <= len(personajes) and 1 <= num_pj2 <= len(personajes )and num_pj1 != num_pj2:
                personaje1 = personajes[num_pj1 - 1]
                personaje2 = personajes[num_pj2 - 1]
                personaje_fusionado = personaje1 + personaje2
                personajes.append(personaje_fusionado)
                print(f"¡Fusion exitosa! El nuevo persoanje es: {personaje_fusionado}")
            else: 
                print("Seleccion invalida. Asegurate  de elegir personajes valido.")
                
    elif opcion == "3":
        mostrar_personajes(personajes)
        
    elif opcion == "4":
        print("Hasta luego!")
        break
    
    else:
        print("Opcion invalida. Por favor, seleccione una opcion valida")
        

while True:
    input("Juego terminado.")


        
import sqlite3

#conexion a la base de datos

comn = sqlite3.connect("contactos.db")
cursor = comn.cursor()

#crear la tabla de la base de datos

cursor.execute("CREATE TABLE IF NOT EXISTS contacts (id INTERGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT)")

# funcion de mostrar todos los contactos

def mostrar():
    cursor.execute("SELECT * FROM contactos;")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

#funcion para ingresar un nuevo registro en el sistema

def agregar():
    name = input("Ingrese el nombre del contacto: ")
    email = input("Ingrese su email:")

    cursor.execute("INSERT INTO contacts (name,email) VALUES (?,?)", (name,email))

    comn.commit()

    print("contacto agregado con EXITO...")


#funcion para actualizar los datos de la tabla

def actualizar():

    id = int(input("ingrese el id de el perfil a modificar: "))

    cursor.execute("SELECT * FROM contacts WHERE id = ?",(id,))

    contact = cursor.fetchone()

    if contact is None:
        print("no se encontro ningun contacto con ese id")
        return
    
    print("Contacto actual")
    print("id:",contact[0])
    print("nombre:",contact[1])
    print("email:",contact[2])

    name = input("Ingrese el nuevo nombre del contacto: ")

    email = input("Ingrese el nuevo email:")

    if not name and not email:
        print("no se ingreso ningun valor a actualizar")

        return

    if name:
        cursor.execute('UPDATE contacts SET name = ?  WHERE id = ?', (name,id))
    
    elif email:
        cursor.execute('UPDATE contacts SET email = ?  WHERE id = ?', (name,id))

    comn.commit()

    print("contacto acutalizado con exito...")


#funcion para eliminar contactos
    
def eliminar():
    id = input("ingresa la id del contacto a eliminar")
    cursor.execute("DELETE FROM contacts WHERE id = ?",(id,))
    comn.commit()
    print("contacto eliminado correctamente..")

#menu de la aplicacion

while True:
    print("1. mostrar")
    print("2. agregar")
    print("3. actualizar")
    print("4. borrar")
    print("5. salir")

    opcion = int(input("ingrese una opcion: "))

    if opcion == "1":
        mostrar()
    elif opcion == "2":
        agregar()
    elif opcion == "3":
        actualizar()
    elif opcion == "4":
        eliminar()
    elif opcion == "5":
        break
    else:
        print("ingrese una opcion valida.")


comn.close()


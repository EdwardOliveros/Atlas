import sqlite3
conection=sqlite3.connect('C:\\Atlas\\Atlas.db')

mycursor=conection.cursor()

def agregar():
    NumeroDocumento=int(input("Ingrese el numero del documento del nuevo usuario: "))
    tipodocumento=input("Ingrese el tipo de documento: ")
    nombre=input("ingrese el nombre: ")
    apellido=input("ingrese el apellido: ")
    correo=input("ingrese el correo: ")
    contraseña=input("ingrese la contraseña: ")

    sentencia= f"INSERT INTO Usuario VALUES ('{NumeroDocumento}', '{tipodocumento}', '{nombre}', '{apellido}', '{correo}', '{contraseña}', 'Activo')"
    mycursor.execute(sentencia)
    conection.commit()
    print("Registro Creado Con Exito")

def modificar(tabla, campo, dato, id):
    sentencia=f"UPDATE {tabla} SET {campo}='{dato}' WHERE idusuario={id}"
    mycursor.execute(sentencia)
    conection.commit()
    print("Modificación Exitosa")

def consultar(campo1, tabla, campo2, operador, dato):
    sentencia=f"SELECT {campo1} FROM {tabla} WHERE {campo2}{operador} '{dato}'"
    mycursor.execute(sentencia)
    print(mycursor.execute(sentencia).fetchall())

agregar()

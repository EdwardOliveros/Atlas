import sqlite3
conection=sqlite3.connect('C:\\atlasdb.db')

mycursor=conection.cursor()

def agregar(tabla, id, nombre, apellido, rol, correo, contraseña, numerodocumento, tipodocumento, estado):
    sentencia= f"INSERT INTO {tabla} VALUES ('{id}', '{nombre}', '{apellido}', '{rol}', '{correo}', '{contraseña}', '{numerodocumento}', '{tipodocumento}', '{estado}')"
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

#agregar("usuario", 2, "edward", "oliveros", "administrador", "santiago.oliveros07@gmail.com", "1234567", 12345678, "CC", "Habilitado")
#modificar("usuario", "estadousuario", "Activo", "2")
#consultar("*", "usuario", "idusuario", "=", 31)

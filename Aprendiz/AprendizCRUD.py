import sqlite3
conection=sqlite3.connect('C:\\Atlas\\Atlas.db')

mycursor=conection.cursor()

def agregar():

    NumeroDocumento = int(input("Ingrese el Numero de Documento del Aprendiz: "))
    rol = int(input("Ingrese el numero de rol que asignara al aprendiz: "))
    ficha = int(input("Ingrese el numero de ficha a la que pertence el aprendiz: "))
    programa = input("Ingrese el nombre de ficha: ")

    sentencia= f"INSERT INTO Aprendiz (nDocumentoUsuarioAprendiz, idTipoRolAprendiz, fichaAprendiz, programaAprendiz) VALUES ('{NumeroDocumento}', '{rol}', '{ficha}', '{programa}')"
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
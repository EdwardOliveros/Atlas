import sqlite3
conection=sqlite3.connect("C:\\CAESAR\\basedatos2.0\\DB2.0")

mycursor=conection.cursor()

def agregar (tabla,id,nombre,Cantidad):
    sentencia=f"INSERT INTO {tabla} VALUES ('{id}','{nombre}','{Cantidad}')"
    mycursor.execute(sentencia)
    conection.commit()
    print('AGREGADO CON EXITO!!!')

def modificar (tabla, campo, dato, id):
    sentencia=f"UPDATE {tabla} SET {campo}='{dato}' WHERE id={id}"
    mycursor.execute(sentencia)
    conection.commit()
    print('ACTUALIZADO !!!')

def consultar(campo1,tabla,campo2,operador,dato):
    sentencia=f"SELECT {campo1} FROM {tabla} WHERE {campo2}{operador} '{dato}'"
    mycursor.execute(sentencia)
    print(mycursor.execute(sentencia).fetchall())




#agregar("Hotel",5556, "Vegeta", 15)
#consultar("*","Hotel","id","+",1)
modificar("hotel","nombre","OlimpUs","222")

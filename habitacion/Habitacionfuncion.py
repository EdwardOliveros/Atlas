import sqlite3

con=sqlite3.connect("C:\\CAESAR\\basedatos2.0\\DB2.0")
micursor=con.cursor()


def agregar(tabla,id,):
    sentencia=f"INSERT INTO {tabla} VALUES ('{id}') "
    micursor.execute(sentencia)
    con.commit()
    print('AGREGADO CON EXITO')


def modificar(tabla,campo1,dato,id):
    sentencia=f"UPDATE {tabla} SET {campo1}='{dato}' WHERE id={id}"
    micursor.execute(sentencia)
    con.commit()
    print("LISTO")

def consultar(campo1,tabla,campo2,):
    sentencia=f"SELECT {campo1} FROM {tabla} WHERE '{campo2}'"
    micursor.execute(sentencia)
    con.commit()
    print(micursor.execute(sentencia).fetchall())

def eliminar(tabla,campo,dato):
    sentencia=f"DELETE FROM {tabla} WHERE {campo}='{dato}'"
    micursor.execute(sentencia)
    con.commit()
    print('ELIMINADO PROOO !!!')



#agregar("habitacion",567)
#modificar("habitacion","id",1,2)
#consultar("*","Habitacion",1)
eliminar("Habitacion","id",567)


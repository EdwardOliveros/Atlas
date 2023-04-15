import sqlite3

cone= sqlite3.connect("C:\\CAESAR\\basedatos2.0\\DB2.0")
micursor=cone.cursor()
    
def agregar(tabla,campo,nombre,estado):
    sentencia=f"INSERT INTO {tabla} VALUES ('{campo}','{nombre}','{estado}')"
    micursor.execute(sentencia)
    cone.commit()
    print('AGREGADO CON EXITO!!!')

agregar('Tipohabitacion','A-002','Sencilla','Disponible')
#miselect(con,'alumno','email','=','dbrabon2@irs.gov')
#miselect(con,'alumno','id','<=',5)

def modificar (tabla, campo, dato, nombre, estado):
    
    sentencia=f"UPDATE {tabla} SET {campo} WHERE '{dato}{nombre}{estado}'"
    micursor.execute(sentencia)
    cone.commit()
    print('ACTUALIZADO !!!')

modificar('Tipohabitacion','id','A-003','Suite')
#DELETE FROM table_name WHERE condition;
'''def eliminar(conexion,tabla,campo,dato):
    micursor=conexion.cursor()
    sentencia=f"DELETE FROM {tabla} WHERE {campo}='{dato}'"
    micursor.execute(sentencia)
    con.commit()
    print('Eliminación exitosa !!!!')

eliminar(con,'alumno','id',3)'''
    
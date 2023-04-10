from Servicio import *
import sqlite3 

con=sqlite3.connect('Base Datos/Servicio.db') 
micursor=con.cursor()
     
def insertar(conexion,tabla,id,nombre,descripcion):
    micursor=conexion.cursor()
    sentencia=f"INSERT INTO {tabla} (id,nombre,descripcion) VALUES ({id},'{nombre}','{descripcion}')"
    micursor.execute(sentencia)
    con.commit()
    print('Insercion exitosa !!!!!')
    
def modificar(conexion,tabla,campo,dato,id):
    micursor=conexion.cursor()
    sentencia=f"UPDATE {tabla} SET {campo}='{dato}' WHERE id={id}"
    micursor.execute(sentencia)
    con.commit()
    print('Modificacion exitosa !!!!!')
  
def eliminar(conexion,tabla,dato):
    micursor=conexion.cursor()
    sentencia=f"DELETE FROM {tabla}  WHERE id={dato}"
    micursor.execute(sentencia)
    con.commit()
    print('Eliminacion exitosa !!!!!')

def consultar(conexion,tabla,dato):
    micursor=conexion.cursor()
    sentencia=f"SELECT * FROM {tabla} WHERE id={dato} "
    lista=micursor.execute(sentencia)

    servicios=[]
    for fila in lista:
        id=fila[0]
        nombre=fila[1]
        descripcion=fila[2]

        ob=Servicio(id,nombre,descripcion)
        servicios.append(ob)

    for p in servicios:
        print(p.getNombre())
    


    print('Consulta exitosa !!!!!')


#insertar(con, 'Servicios', 8, 'Transporte','Taxis Libres')
#modificar(con,'Servicios', 'descripcion','Uber',8)
#eliminar(con,'Servicios', 8)
#consultar(con,'Servicios',7)
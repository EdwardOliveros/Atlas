from Factura import *
import sqlite3 

con=sqlite3.connect('Base Datos/Factura.db') 
micursor=con.cursor()
     
def insertar(conexion,tabla,id,fecha,costoTotal,idReserva,idServicio,metodoPago,idUsuarioSistema,idPlan):
    micursor=conexion.cursor()
    sentencia=f"INSERT INTO {tabla} (id,fecha,costoTotal,idReserva,idServicio,metodoPago,idUsuarioSistema,idPlan) VALUES ({id},'{fecha}','{costoTotal}',{idReserva},{idServicio},'{metodoPago}',{idUsuarioSistema},{idPlan})"
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

    facturas=[]
    for fila in lista:
        id=fila[0]
        fecha=fila[1]
        costoTotal=fila[2]
        idReserva=fila[3]
        idServicio=fila[4]
        metodoPago=fila[5]
        idUsuarioSistema=fila[6]
        idPlan=fila[7]
        ob=Factura(id,fecha,costoTotal,idReserva,idServicio,metodoPago,idUsuarioSistema,idPlan)
        facturas.append(ob)

    for p in facturas:
        print(p.getCostoTotal())
    


    print('Consulta exitosa !!!!!')


#insertar(con,'Facturas',1001,'8/28/2022','$6,89',1001,1001,'maestro',1001,1001)
#modificar(con,'Facturas', 'costoTotal','$19.94',1001)
#eliminar(con,'Facturas',1001)
#consultar(con,'Facturas',1000)
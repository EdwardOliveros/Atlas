from usuario import *
import sqlite3
lista=[]

with sqlite3.connect('C:\\atlasdb.db') as con:
    mycursor=con.cursor()
    new_sql="select * from usuario"
    #print(mycursor.execute(new_sql).fetchall())
    lista=mycursor.execute(new_sql).fetchall()

usuarios=[]
for i in lista:
    idusuario=i[0]
    nombreusuario=i[1]
    apellidousuario=i[2]
    rolusuario=[3]
    correousuario=[4]
    contraseñausuario=[5]
    numerodocumentousuario=[6]
    tipodocumentousuario=[7]
    estadousuario=[8]
    objeto=usuario(idusuario, nombreusuario, apellidousuario, rolusuario, correousuario, contraseñausuario, numerodocumentousuario, tipodocumentousuario, estadousuario)
    usuarios.append(objeto)

print(usuarios)

for i in usuarios:
    print(i.getNombre())
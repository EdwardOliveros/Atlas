import sqlite3
conection=sqlite3.connect('C:\\Atlas\\Atlas.db')

mycursor=conection.cursor()

def agregar():

    print("Bienvenido a la funcion Agregar de la tabla Aprendiz \n")

    NumeroDocumento = int(input("Ingrese el Numero de Documento del Aprendiz: "))
    rol = int(input("Ingrese el numero de rol que asignara al aprendiz: "))
    ficha = int(input("Ingrese el numero de ficha a la que pertenece el aprendiz: "))
    programa = input("Ingrese el nombre de ficha: ")

    sentencia= f"INSERT INTO Aprendiz (nDocumentoUsuarioAprendiz, idTipoRolAprendiz, fichaAprendiz, programaAprendiz) VALUES ('{NumeroDocumento}', '{rol}', '{ficha}', '{programa}')"
    mycursor.execute(sentencia)
    conection.commit()

    print("Registro Creado Con Exito \n")

def modificar():

    campo=input("ingrese el campo:")
    dato=input("ingrese el dato: ")
    id=int(input("ingrese el identificador o llave primaria"))

    sentencia=f"UPDATE Aprendiz SET {campo}='{dato}' WHERE idusuario={id}"
    mycursor.execute(sentencia)
    conection.commit()
    print("Modificación Exitosa")

def consultar():

    campo1=input("ingrese el campo que desea consultar: ")
    operador=input("ingrese el operador: ")
    dato=input("ingrese el dato que sera operado: ")

    sentencia=f"SELECT * FROM Aprendiz WHERE {campo1} {operador} '{dato}'"
    mycursor.execute(sentencia)
    print(mycursor.execute(sentencia).fetchall())

def mostrartabla():
    sentencia=f"SELECT * FROM Aprendiz"
    mycursor.execute(sentencia)
    print(mycursor.execute(sentencia).fetchall())


opcion = int(input("\n Bienvenido a CRUD Aprendiz \n Favor seleccione la opcion que desea realizar: \n \n 1.Agregar \n 2.Mostrar todos los registros \n 3.Consultar Registro \n 4.Modificar \n 0.Salir \n Respuesta:"))
while opcion != 0:
    if opcion == 1:
        agregar()
        
    elif opcion == 2:
        mostrartabla()
        
    elif opcion == 3:
        consultar()
    
    elif opcion == 4:
        modificar
        
    else:
        print("Porfavor Ingresar una opcion valida!")
    
    opcion = int(input("\n Bienvenido a CRUD Aprendiz \n Favor seleccione la opcion que desea realizar: \n \n 1.Agregar \n 2.Mostrar todos los registros \n 3.Consultar Registro \n 4.Modificar \n 0.Salir \n Respuesta:"))

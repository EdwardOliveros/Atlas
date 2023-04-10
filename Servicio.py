class Servicio: 
    def __init__(self,id,nombre,descripcion):
        self.__id=id
        self.__nombre=nombre
        self.__descripcion=descripcion

    #Geters and setters id
    def getIdServicio(self):
        return self.__id
    def setIdServicio(self,id):
        self.__id=id
    def deleteIdServicio(self):
        del self.__id
    
    #Geters and setters nombre
    def getNombre(self):
        return self.__nombre
    def setNombre(self, nombre):
        self.__nombre=nombre
    def deleteNombre(self):
        del self.__nombre
    
    #Geters and setters descripcion
    def getDescripcion(self):
        return self.__descripcion
    def setDescripcion(self,descripcion):
        self.__descripcion=descripcion
    def deleteDescripcion(self):
        del self.__descripcion
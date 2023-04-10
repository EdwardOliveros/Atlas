class Plan:
    def __init__(self,id,idServicio,nombre,descripcion,precio,estado):
        self.__id = id
        self.__idServicio = idServicio
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.estado = estado

    def getIdPlan(self):
        return self.__id
    def setIdPlan(self):
        self.__id = id
    def deleteIdPlan(self):
        del self.__id

    def getidServicio(self):
        return self.__idServicio
    def setidServicio(self):
        self.__idServicio = idServicio
    def deleteidServicio(self):
        del self.__idServicio

    def getnombre(self):
        return self.nombre
    def setnombre(self):
        self.nombre = nombre
    def deletenombre(self):
        del self.nombre

    def getdescripcion(self):
        return self.descripcion
    def setdescripcion(self):
        self.descripcion = descripcion
    def deletedescripcion(self):
        del self.descripcion
    
    def getprecio(self):
        return self.precio
    def setprecio(self):
        self.precio = precio
    def deleteprecio(self):
        del self.precio
    
    def getesatdo(self):
        return self.estado
    def setestado(self):
        self.estado = estado
    def deleteestado(self):
        del self.estado
        
class Factura: 
    def __init__(self,id,fecha,costoTotal,idReserva,idServicio,metodoPago,idUsuarioSistema,idPlan):
        self.__id=id
        self.__fecha=fecha
        self.__costoTotal=costoTotal
        self.__idReserva=idReserva    
        self.__idServicio=idServicio
        self.__metodoPago=metodoPago
        self.__idUsuarioSistema=idUsuarioSistema
        self.__idPlan=idPlan   

    #Geters and setters id
    def getIdFactura(self):
        return self.__id
    def setIdFactura(self,id):
        self.__id=id
    def deleteIdFactura(self):
        del self.__id
    
    #Geters and setters Fecha
    def getFecha(self):
        return self.__fecha
    def setFecha(self, fecha):
        self.__fecha=fecha
    def deleteFecha(self):
        del self.__fecha
    
    #Geters and setters costoTotal
    def getCostoTotal(self):
        return self.__costoTotal
    def setCostoTotal(self,costoTotal):
        self.__costoTotal=costoTotal
    def deleteCostoTotal(self):
        del self.__costoTotal

    #Geters and setters idReserva
    def getIdReserva(self):
        return self.__idReserva
    def setIdReserva(self,idReserva):
        self.__idReserva=idReserva
    def deleteIdReserva(self):
        del self.__idReserva
    
    #Geters and setters idServicio
    def getIdServicio(self):
        return self.__idServicio
    def setIdReserva(self,idServicio):
        self.__idServicio=idServicio
    def deleteIdServicio(self):
        del self.__idServicio
    
    #Geters and setters metodoPago
    def getMetodoPago(self):
        return self.__metodoPago
    def setMetodoPago(self,metodoPago):
        self.__metodoPago=metodoPago
    def deleteMetodoPago(self):
        del self.__metodoPago
    
    #Geters and setters idUsuarioSistema
    def getIdUsuarioSistema(self):
        return self.__idUsuarioSistema
    def setIdUsuarioSistema(self,idUsuarioSistema):
        self.__idUsuarioSistema=idUsuarioSistema
    def deleteIdUsuarioSistema(self):
        del self.__idUsuarioSistema
    
    #Geters and setters idPlan
    def getIdPlan(self):
        return self.__idPlan
    def setIdPlan(self,idPlan):
        self.__idPlan=idPlan
    def deleteIdPlan(self):
        del self.__idPlan
    


class Reserva:

    def __init__(self,id,fechaInicio,fechaFin,precio,idCliente,idHabitacion,estado,idPlan):
        self.__id = id
        self.fechaInicio = fechaInicio
        self.fechaFin = fechaFin
        self.precio = precio
        self.idCliente = idCliente
        self.idHabitacion = idHabitacion
        self.estado = estado
        self.idPlan = idPlan

    def getIdReserva(self):
        return self.__id
    def setIdReserva(self):
        self.__id = id
    def deleteIdPlan(self):
        del self.__id

    def getfechaInicio(self):
        return self.fechaInicio
    def setfechaInicio(self):
        self.fechaInicio = fechaInicio
    def deletefechainicio(self):
        del self.fechaInicio

    def getfechaFin(self):
        return self.fechaFin
    def setfechaFin(self):
        self.fechaFin = fechaFin
    def deletefechaFin(self):
        del self.fechaFin

    def getprecio(self):
        return self.precio
    def setprecio(self):
        self.precio = precio
    def deleteprecio(self):
        del self.precio

    def getidCliente(self):
        return self.idCliente
    def setIdPlan(self):
        self.idCliente = idCliente
    def deleteIdPlan(self):
        del self.idCliente

    def getidHabitacion(self):
        return self.idHabitacion
    def setidHabitacion(self):
        self.idHabitacion = idHabitacion
    def deleteidHabitacion(self):
        del self.idHabitacion

    def getestado(self):
        return self.estado
    def setestado(self):
        self.estado = estado
    def deleteestado(self):
        del self.estado

    def getidPlan(self):
        return self.idPlan
    def setidPlan(self):
        self.idPlan = idPlan
    def deleteidPlan(self):
        del self.idPlan

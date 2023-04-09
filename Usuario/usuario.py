class usuario:
    def __init__(self, idusuario, nombreusuario, apellidousuario, rolusuario, correousuario, contraseñausuario, numerodocumentousuario, tipodocumentousuario, estadousuario):
        self.idusuario=idusuario
        self.nombreusuario=nombreusuario
        self.apellidousuario=apellidousuario
        self.rolusuario=rolusuario
        self.correousuario=correousuario
        self.contraseñausuario=contraseñausuario
        self.numerodocumentousuario=numerodocumentousuario
        self.tipodocumentousuario=tipodocumentousuario
        self.estadousuario=estadousuario
        
    def getNombre(self):
        return self.nombreusuario